import threading
import queue

def process_queue(my_queue):
    while (True):
        print("worker thread will now wait for item...")
        item = my_queue.get()
        print("worker thread got a work item ...")
        print("working on ", item)
        print("worker thread finished ....")

# thread safe
q = queue.Queue()
# process_queue(q) # -- blocking the program
MAX_THREADS = 100
for i in range(MAX_THREADS):
    worker = threading.Thread(target=process_queue, args=(q,))
    worker.setDaemon(True)
    worker.start()
while True:
    item = input("Insert work item: (or Exit)")
    if item.upper() == 'EXIT':
        break
    print("putting item inside queue ...")
    q.put(item)



