def inner_func(x,y):
    def inner_add():
        return x+y
    def inner_div():
        return y/x
    print(inner_add() + inner_div())

inner_func(9,7)