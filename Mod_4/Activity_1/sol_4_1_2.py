# Write a lambda function to cube every element of a list.

    # Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

cubed_num = lambda x: [i**3 for i in x]
print(cubed_num([3,6,9,2]))