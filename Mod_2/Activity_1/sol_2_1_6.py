# arb_mean — Accepts any number of
# integers and prints their average.

def arb_mean(*args):
    total = 0
    for i in args:
        total += i
        print(i/len(args))

arb_mean(1,5,9,7,85,112,3)