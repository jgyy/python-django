"""Scope"""
X = 25
NAME = "This is a global name"
MY_LIST = [1, 2, 3, 4]


def my_func(func_x):
    """my function"""
    name = "sammy"
    print('x is:', func_x)
    func_x = 50
    print('local x changed to:', func_x)

    def hello():
        """hello function"""
        print("Hello " + name)

    hello()
    return func_x


print([X, NAME])
print(my_func(X))
print([MY_LIST, type(MY_LIST)])
