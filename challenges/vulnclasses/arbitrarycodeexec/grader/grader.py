def grade(arg, key):
    if "flag{h0ws_th4t_sh3ll_f33l1n?}".lower() == key.lower():
        return True, "That was easy wasn't it?"
    else:
        return False, "Try harder."
