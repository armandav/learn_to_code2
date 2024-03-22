def print_disclaimer():
    print("#    This is to show even or odd ")
    print("#     My disclaimer line 2 ")

def print_fmt_msg(key, value="DDDDDDDDD", param2=""):
    print("##################################################")
    print("#  key=", key, ", value=", value)
    print_disclaimer()
    print("#-------------------------------------------------")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

x = is_even(11)
print_fmt_msg(11, x)
print_fmt_msg(10, is_even(10))
print_fmt_msg("This is example key", "Example value")
print_fmt_msg("This is example key for default value")
print_fmt_msg(param2="arg3", value="arg2", key="My Key")