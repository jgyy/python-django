"""My Module"""
S = "GLOBAL VARIABLE!"


def other(func):
    """
    :param func: other function
    """
    print("HELLO")

    def wrap_func():
        """Wrapper Function"""
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


@other
def func_in_module(name="Jose"):
    """Function inside a module"""
    my_local = 10
    print("I AM INSIDE THE MYMODULE.PY FILE! " + str(my_local))
    print(locals())
    print(globals()['S'])

    def greet():
        """
        :return: greet
        """
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        """
        :return: welcome
        """
        return "THIS STRING IS INSIDE WELCOME!"

    if name == "Jose":
        return greet()
    return welcome()


func_in_module()
