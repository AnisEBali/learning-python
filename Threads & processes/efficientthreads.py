import threading
import time

#The issue is creating multiple threads is very tedious 
def longSquare(num,results):
    time.sleep(1)
    results[num] = num**2

results = {}
# Instead we're gonna use a for loop to create many threads at once!:
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range (0,10)]

# We can for loop the start and join too.
[t.start() for t in threads]
[t.join() for t in threads]

print(results)