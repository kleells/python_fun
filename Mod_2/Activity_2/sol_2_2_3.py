# Write a function that returns the first n elements
# in the Fibonacci Sequence. 
# Fibonacci Sequence is when a series of numbers add upon themselves
# the number if the sequence added to the previous number
# Ex. 0,1,1,2,3,5,8,12,21,34,55,89
# 0 + 1 = 1, 1 + 1 = 2, 2 + 1 = 3, 3 + 2 = 5, etc, etc


def fib_seq(i):
    # BASE CASE (because the sequense won't work otherwise)
    if i<=1:
        return i

    # RECURSIVE CASE
    else:
        return (fib_seq(i-1)+fib_seq(i-2))

i=10
for n in range (i):
    print(fib_seq(n))
