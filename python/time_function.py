import time


print(time.ctime(0)) # convert a time expressed in second since epoch to a readable string
                     # epoch = when your computer thinks time begun ( referance point)


print(time.time() ) # return current seconds since epoch

print(time.ctime(time.time())) # to get current date and time

# to get local time but here you cutomize it.

time_object=time.localtime()
local_time= time.strftime("%B %d %Y :%H:%M:%S ", time_object)
print(local_time)

time_utc = time.gmtime()
print(time_utc)


time_string = "20 April, 2024"
time_read=time.strptime(time_string, "%d %B, %Y")

print(time_read)



# asctime() 
# parameter is a tuple which as an output gives string
# takes 9 values
# ( year, month, day, hours, minutes, secs, day of the week, day of the year, dst)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_2 = time.asctime(time_tuple)

print(type(time_string_2))
print(time_string_2)