import time

# decorator - function which calls another function
def mytimer(your_function):
    def executor(*args, **kwargs):
        start_time = int(round(time.time() * 1000))
        your_function(*args, **kwargs)
        end_time = int(round(time.time() * 1000))
        print(f' execution time : {end_time - start_time}')
    return executor

@mytimer
def print_with_stars(msg):
    print(f'********* {msg}*********')
    input()
print_with_stars("hello")
