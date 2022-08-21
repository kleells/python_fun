# Write a function that prints the natural numbers from 1 to n.

def nat_num(lowNum, highNum):
    # BASE CASE
    if lowNum > highNum:
        return
    
    # RECURSIVE CASE
    else:
        print(lowNum)
        nat_num(lowNum + 1, highNum)

n=9
nat_num(1, n)