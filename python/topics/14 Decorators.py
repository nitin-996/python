def some_decorator(wrapper_function):
    def wrapper():
        print("so sth before calling wrapped function")
        wrapper_function()
        print("do sth after calling wrapped function")
    return wrapper
    

def foot():
    print("foot fnuction")


# we can do this like

f = some_decorator(foot)

f()


# IN PYTHON WE CAN DO IT ANOTHER WAY ALSO

@some_decorator
def foot2():
    print("this is foot2")


foot2()