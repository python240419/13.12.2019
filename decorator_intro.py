# decorator - function which calls another function
def password(your_function):
    def executor():
        print("before your_function ===========")
        pwd = input("Enter password: ")
        if pwd == "12345":
            your_function()

        print("after your_function ===========")
    return executor

@password
def hello_func():
    print("hello world!")
hello_func()
