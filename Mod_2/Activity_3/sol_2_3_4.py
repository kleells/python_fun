# recursive_factorial — Uses recursion to
# find the factorial of an integer.

def find_fact(num):
    if num == 1:
        return 1

    else:
        return num * find_fact(num-1)

n=4
print(find_fact(n))