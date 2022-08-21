# alias_arb_args — Should be arb_args
# but assigned an alias. Remember,
# variables can hold functions in Python
# just like they can in JS. Alternatively,
# you can call a function from inside another function.

def arb_args(*args):
    for x in args:
        print(x)

alias_arb_args = arb_args

alias_arb_args(4, False, "Way to go!")