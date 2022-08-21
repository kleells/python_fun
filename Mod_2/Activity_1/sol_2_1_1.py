# arb_args — Takes in any number of arguments 
# and prints them one at a time. 

def arb_args(*args):
    for x in args:
        print(x)

arb_args(4, True, "You've got this")