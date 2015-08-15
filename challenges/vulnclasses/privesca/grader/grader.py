def grade(arg, key):
    if "flag{3sc4l4t3d_r34lly_qu1ckly}".lower() == key.lower():
        return True, "Just because something's simple doesn't mean it's not " \
            "dangerous."
    else:
        return False, "..."
