# arb_longest_string — Accepts any number
# of strings and returns the longest one.

def arb_longest_string(*args):
    long = 0
    longest = ""
    for l in args:
        if len(l) > long:
            long = len(l)
            longest = l
    print(longest)

arb_longest_string("Am I the longest?", "Or, am I the longest?")