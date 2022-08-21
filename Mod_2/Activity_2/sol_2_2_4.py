# Write a function that calculates the value of 'a' to the power of 'b'.
def power(base, exp):
    if exp==1:
        return (base)
    else:
        return base*power(base,exp-1)

base=4
exp=2

print(power(base,exp))
