import time

# sample code
#start_time = int(round(time.time() * 1000))
#input()
#end_time = int(round(time.time() * 1000))
#print(end_time - start_time)

# Exercise:
# write decorator which prints how long took the method to run

# decorator - function which calls another function
def mytimer(your_function):
    def executor():
        start_time = int(round(time.time() * 1000))
        your_function()
        end_time = int(round(time.time() * 1000))
        print(end_time - start_time)
    return executor

@mytimer
def hello_func():
    print("hello world!")
    input("enter a number :")
hello_func()
