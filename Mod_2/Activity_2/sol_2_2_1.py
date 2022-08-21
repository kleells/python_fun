# Write a program that takes a positive number 
# as an argument and prints the numbers from n to zero.

def pos_countdown(n):
    
    # BASE CASE
    if n==0:
        return

    # RECURSIVE CASE
    else:
        print(n)
        pos_countdown(n-1)

n=7
pos_countdown(n)

