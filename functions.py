def print_disclaimer():
    print("#    This is to show even or odd ")
    print("#     My disclaimer line 2 ")

def print_fmt_msg(msg):
    print("##################################################")
    print("#  ", msg)
    print_disclaimer()
    print("#-------------------------------------------------")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

x = is_even(11)
print_fmt_msg(x)
print_fmt_msg(is_even(10))
print_fmt_msg("This is example message")