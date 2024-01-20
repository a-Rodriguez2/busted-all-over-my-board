import cv2
import os 
import time

def adjust_brightness_contrast(frame, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        
        frame = cv2.addWeighted(frame, alpha_b, frame, 0, gamma_b)
    
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        
        frame = cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)

    return frame

def save_snapshot(frame, count):
    filename = f"snapshot_{count}.png"
    cv2.imwrite(filename, frame)
    print(f"Snapshot saved as '{filename}'")





def zoom_frame(frame, zoom_factor):
    if zoom_factor <= 1:
        return frame
    height, width = frame.shape[:2]
    new_height, new_width = int(height / zoom_factor), int(width / zoom_factor)
    start_row, start_col = height//2 - new_height//2, width//2 - new_width//2
    cropped_frame = frame[start_row:start_row+new_height, start_col:start_col+new_width]
    return cv2.resize(cropped_frame, (width, height))
def main():
    cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    # Set camera properties
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # Create a window
    cv2.namedWindow("frame")

    # Neutral values for trackbars
    neutral_value = 127

    # Create trackbars for zoom, contrast, and brightness
    cv2.createTrackbar('Zoom', 'frame', 1, 4, lambda x: None)
    cv2.createTrackbar('Contrast', 'frame', neutral_value, 2*neutral_value, lambda x: None)
    cv2.createTrackbar('Brightness', 'frame', neutral_value, 2*neutral_value, lambda x: None)

    snapshot_count = 0  # Initialize snapshot counter

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Get current positions of the trackbars
        zoom_level = cv2.getTrackbarPos('Zoom', 'frame')
        contrast = cv2.getTrackbarPos('Contrast', 'frame') - neutral_value
        brightness = cv2.getTrackbarPos('Brightness', 'frame') - neutral_value

        # Apply zoom
        frame = zoom_frame(frame, zoom_level)
    
        # Apply brightness and contrast adjustments
        frame = adjust_brightness_contrast(frame, brightness, contrast)

        # Display the resulting frame
        cv2.imshow("frame", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):  # Save a snapshot when 's' key is pressed
           # Switch to high resolution for the screenshot
           cap.set(cv2.CAP_PROP_FRAME_WIDTH, 8000)
           cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 6000)

           # Wait for camera to adjust, or flush the buffer
           time.sleep(0.5)
           for _ in range(5):
               cap.read()

           # Grab a single frame at high resolution
           ret, high_res_frame = cap.read()
           
           # Apply zoom
           high_res_frame = zoom_frame(high_res_frame, zoom_level)
       
           # Apply brightness and contrast adjustments
           high_res_frame = adjust_brightness_contrast(high_res_frame, brightness, contrast)
           
           if ret:
               save_snapshot(high_res_frame, snapshot_count)
           else:
               print("Error: Could not read high-resolution frame.")

           # Switch back to the standard resolution for the video feed
           cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
           cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

           # Wait for camera to adjust back
           time.sleep(0.5)
           for _ in range(5):
               cap.read()

           snapshot_count += 1

    # Release the capture when everything is done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()