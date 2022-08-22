# recursive_duplicate — Recursively removes all
# adjacent duplicate letters from a string.

def recursive_duplicate(str, i=0):
    # if our string is empty or only has 1 thing, it's got no duplicates
    # if i is at the end of the string, no duplicates are left
    if len(str) <= 1 or i == len(str)-1:
        return str
    
    else:
    # str at current position is same as next position
        if str[i] == str[i+1]:
            return recursive_duplicate(str[0:i]+str[i+1],i)
        else:
        #no duplicate at current position, check next
            return recursive_duplicate(str, i+1)

print(recursive_duplicate("aaaa"))
print(recursive_duplicate("abba"))
print(recursive_duplicate("apple"))
print(recursive_duplicate(""))