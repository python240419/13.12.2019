# decorator - function which calls another function
def wrapper(your_function):
    print("before f2 ===========")

    your_function()

    print("after f2 ===========")

def hello_func():
    print("hello world!")


def math_x():
    x = 10
    print(x)

wrapper(hello_func)
wrapper(math_x)

