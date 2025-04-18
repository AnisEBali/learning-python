import threading
import time
import random

# Chef function: cooks for a customer

def serveCustomer(customerID,ordersReady):
    print(f"Chef starts cooking for {customerID}")
    # Simulate random cooking time:
    time.sleep(random.uniform(0.5,1.5))
    dish = random.choice([
        "This is an exquisite, Michelin star dish!",
        "This is a delicious dish!",
        "This is a nice meal.",
        "It's a bit cold...",
        "It's gross! Yuck!"
    ])
    ordersReady[customerID] = dish
    print(f"Order ready for Customer {customerID}!")

ordersReady = {}
customers = list(range(1,11)) # 10 customers in total

# Create a chef for every customer
chefs = [
    threading.Thread(target=serveCustomer,args=(cust,ordersReady))
    for cust in customers
    # Every chef gets a designated customer assigned
    # ordersReady is where they will store the final dish 
]

# Starttime for all the chefs:
for chef in chefs:
    chef.start()

# Wait until all chefs are done
for chef in chefs:
    chef.join()

print('All orders are served!')
for cid in sorted(ordersReady):
    print(f'Customer {cid}: {ordersReady[cid]}')
# cid = loop-variable for the keys of ordersReady
# ordersReady was set-up with customerID as key & dish as value remember?