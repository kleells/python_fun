
# Problem 1: Write a function flatten_dict to flatten a
# nested dictionary by joining the keys with . character.
# flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})
# {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}

# Hint: You can assume that all dictionary keys will be of
# type string, and that nested dictionaries will only be nested
# one layer deep (a dictionary of dictionaries will not have
# another dictionary nested inside it).

# this code removes an inner dictionary from the outer one in the print
# statement
def flatten_dict(d):
    result = dict()
    for i in d.keys():
        if type(d[i]) == dict:
            # the value is a dictionary, so we must flatten it
            for k,v in d[i].items():
                # make a new key
                new_key = i + "." + k
                #add key: value pair
                result[new_key] = v
        else:
            # add the key:value pair to result dictionary
            result[i] = d[i]
    return result

print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))

# Problem 2: Write a function unflatten_dict to do reverse
# of flatten_dict.
# unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
# {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

# Hint: You can assume that the keys for the dictionary will
# all be of type string, and that you never need to create
# more than one layer of nested dictionary. It may be helpful
# to create an empty dictionary as the value for the outer
# key ('b' in this example), then fill it in iteratively as you
# find keys that belong to that dictionary.

def unflatten_dict(d):
    result = dict()
    for i in d.keys():
        if "." in i:
            # this should become nested
            new_key, sep, inner_key = i.partition(".")
            # create dictionary if not yet created
            if new_key not in result.keys():
                result[new_key] = dict()
            # add elements to inner dictionary
            result[new_key][inner_key] = d[i]
        else:
            #add the key:value pair to the result dictionary
            result[i] = d[i]
    return result

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))



# Write a function treemap() to map a function over nested list.
# treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]

# Hint: Using recursion may make this function easier to code.
# Don't forget to check the type of the element you are iterating over.

def treemap(func, lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = treemap(func, lst[i])
        else:
            lst[i] = func(lst[i])
    return lst

print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))
