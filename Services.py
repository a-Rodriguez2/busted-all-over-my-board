import re

def Post_Process(attempt, iteration):
    try:
        attempt = attempt.replace('\n', '').replace('\r', '').replace(' ', '').replace('\f', '').strip()
        attempt = attempt.replace('O', '0').replace('o', '0').upper()
        attempt = attempt.replace("—", "-").replace("=", "-").replace("_", "-").replace('~', '-')
        attempt = re.sub(r"--+", "-", attempt)
        attempt = re.sub(r"(?<=WSC)[^-]+", "00", attempt)
        attempt = re.sub(r"(?<=-A)[^-]+", "00", attempt)
        print("\tattempt number", iteration, ": ")
        print("\t\tocr result: ", attempt)
        return attempt
    except Exception as e:
        print("Error:", e)
        return attempt
    
def Check_Pattern(attempt):
    pattern = r"^CN-[A-Z0-9]{6}-WSC00-[A-Z0-9]{3}-[A-Z0-9]{4}-A00$"
    if re.match(pattern, attempt):
        print("\t\tmatch")
        return True
    else:
        print("\t\tdoes not match")
        return False