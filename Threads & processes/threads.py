import threading
import time

# FASTER FUNCTION
def anotherLongSquare(num,results):
    time.sleep(1)
    # ^This is to simulate a slow process
    results[num] = num**2

# We're gonna use two threads where each will do the function at the same time as the other
results = {}
# ^ They will put their results in this shared list

t1 = threading.Thread(target=anotherLongSquare, args=(1,results))
# We create a thread with threading.Thread, t1 & t2 as their names
# target = what function they should use
# args is what they input into the function, results where to store the result
t2 = threading.Thread(target=anotherLongSquare, args=(2,results))

# We start both threads at the same time
t1.start()
t2.start()

# Main thread will wait until both threads are finished
t1.join()
t2.join()

print(results)
# -> Results: {1: 1, 2: 4}

#SLOW FUNCTION
def longSquare(num):
    time.sleep(1)
    return num**2

print([longSquare(n) for n in range(0,5)])
# -> Result: [0, 1, 4, 9, 16]