# rrecursive_reverse — Uses recursion to reverse a string.

def recursive_reverse(str, i=0):
    # if string is empty case
    if len(str)==0:
        return ""
    
    # BASE CASE
    elif i == len(str)-1:
        return str[0]

    # RECURSIVE CASE
    else:
        return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("tried"))
print(recursive_reverse("kayak"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))
