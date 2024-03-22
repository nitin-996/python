# multiprocessing = running tasks in parrallel on diffrent cpu cores, Bypasses GIL used for thread

# multiprocessing = it is better for cpu bound tasks
#multithreading = it is better for io bound tasks



from multiprocessing import Process, cpu_count
import time

start_time = time.perf_counter()

def count_1(num):
    count = 0
    while count < num:
        count += 1
        # print(count)

print(cpu_count())     


a = Process(target=count_1, args=(250000,))
b = Process(target=count_1, args=(250000,))
c = Process(target=count_1, args=(250000,))
d = Process(target=count_1, args=(250000,))   

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()


end_time = time.perf_counter()

print("finished in:", end_time - start_time, "sec")
