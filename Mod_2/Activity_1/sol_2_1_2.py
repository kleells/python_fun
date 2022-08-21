# inner_func — Takes in two integers. Two nested 
# functions should perform separate, distinct math 
# operations using the integers. The result of both 
# nested functions should then be added together and printed.

def inner_func(x,y):
    def inner_add():
        return x+y
    def inner_div():
        return y/x
    print(inner_add() + inner_div())

inner_func(9,7)