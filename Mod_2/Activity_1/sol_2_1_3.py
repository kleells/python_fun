# lunch_lady — Takes in two strings: a student's name 
# and their lunch preference. The function should print 
# both strings. If a lunch preference is not given, 
# "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
    print(f"Hello {name} your lunch today is {lunch}.")

lunch_lady("Peter")
