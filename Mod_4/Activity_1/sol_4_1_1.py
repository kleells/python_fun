# Write a lambda function to sort a list of tuples in
# ascending order according to the number in the second
# position of each tuple.

    # Unsorted list of tuples: [('English', 88), ('Science', 90),
    # ('Maths', 97), ('Social sciences', 82)]

    # Sorted list of tuples: [('Social sciences', 82), ('English', 88),
    # ('Science', 90), ('Maths', 97)]

grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# use the sorted() method, set 1st parameter(the iterable)
# to grades, the 2nd(the key) to lambda

sorted_grades = sorted(grades, key = lambda score: score[1])
print(sorted_grades)