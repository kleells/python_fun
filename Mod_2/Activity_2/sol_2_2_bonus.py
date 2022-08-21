# Write a function that when given two numbers,
# finds their greatest common divisor.

def gcd(a, b):
    if(b==0):
        return a

    else:
        return gcd(b, a%b)

a=76
b=33

print(gcd(a,b))
