def grade(arg, key):
    if "flag{y0u_l34k3d_m3!}".lower() == key.lower():
        return True, "Infoleaks are the gateway to further exploitation."
    else:
        return False, "How can you make the program behave in a way not " \
            "intended by the programmer?"
