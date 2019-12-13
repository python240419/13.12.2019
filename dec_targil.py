import time

# sample code
start_time = int(round(time.time() * 1000))
input()
end_time = int(round(time.time() * 1000))
print(end_time - start_time)

# Exercise:
# write decorator which prints how long took the method to run
