# thread = a flow of execution, like a separate order of instructions.
#            howerver each thread takes a turn running to archive concurrency
#             GIL (global interpreter lock),
#              allows only one thread to hold the control of the python interpreter at any one time




# cpu bound = programe/task spends most of its time waiting for internal events ( cpu intensive)
                 # use multiprocessing

# io bound = program/task spends most of its time waiting for external events( user input, web scraping)
                     # use multithreading

# using multithreading we can run multiple threads but it will not be parrallel , it will be concurrently.
# https://www.geeksforgeeks.org/multithreading-python-set-1/

import threading
import time

print(threading.active_count()) # intially single thread was working
print(threading.enumerate())

def eat_breakfast():
   time.sleep(3)
   print("you eat breakfast")


def drink_coffee():    
   time.sleep(5)
   print("you drink coffee")


x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

x.join()
y.join()

print(threading.active_count())  # now total three thread are working
print(time.perf_counter())
# eat_breakfast()   
# drink_coffee()




# daemon thread = a thread that runs in the background , not importanct program to run.
# your program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normally be killed, stay alive until task is complete


# example :background tasks, garbage collection, waiting for input, long running process.

def timer():
   print()
   count=0
   while True:
      time.sleep(1)
      count += 1
      print("logged in for:", count , "seconds")


z = threading.Thread(target=timer , daemon=True)      
z.start()

# z.setDaemon(False) 

print(z.isDaemon()) # to check if it is a daemon thread or not

answer = input(" do you want to exit?")


