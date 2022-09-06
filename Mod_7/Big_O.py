# analyze the complexity of each

list_of_values = ['a', 'b', 'c', 'd', 'e']

def function1(values):
    for value in values:
        print(value)

def function2(values):
    print(values[0])
    print(values[1])

def function3(values):
    for x in values:
        for y in values:
            print(x, y)

def function4(values):
    for i in range(4):
        print("Python is great")

    print("Software Engineering is awesome!")
    print("Software Engineering is awesome!")

    for value in values:
        print(value)

    for value in values:
        print(value)

# It may be helpful to comment out all of the functions beside the function you are focusing on. This can help with determining the output of the function you are analyzing.

function1(list_of_values)
function2(list_of_values)
function3(list_of_values)
function4(list_of_values)