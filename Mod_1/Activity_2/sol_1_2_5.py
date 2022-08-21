# Implement a for loop that iterates through each
# item in the movie_list. 
# If the item is a blueberry (or another fruit),
# print "item is a fruit and not movie"; 
# if the item is a car manufacturing company like Toyota,
# print "item is a car and not a movie"; 
# otherwise, just print the movie in the list:

movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

for item in movie_list:
  if item == "blueberries":
    print("That's a fruit, not a movie")
  elif item == "Toyota":
    print("That's a car, not a movie")
  else:
    print(item)