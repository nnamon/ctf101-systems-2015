def grade(arg, key):
    if "flag{crash}".lower() == key.lower():
        return True, "Denial of service attacks are boring."
    else:
        return False, "Try crashing the program."
