def grade(arg, key):
    if "flag{1nn0c3nt_th1nk_4ga1n}".lower() == key.lower():
        return True, "Just because something's simple doesn't mean it's not " \
            "dangerous."
    else:
        return False, "..."
