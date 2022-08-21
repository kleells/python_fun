# Write a function that checks whether a string
# is a palindrome or not. The program should take
# in a string and return True if the string is a
# palindrome and False if not.

def palindrome_test(str):
    # BASE CASE
    if len(str) < 2:
        return True

    # RECURSIVE CASE
    else:
        if str[0]  == str [-1]:
            return palindrome_test(str[1:-1])
        else:
            return False

# test_word = 'salad'
test_str = 'rotator'
print(palindrome_test(test_str))
