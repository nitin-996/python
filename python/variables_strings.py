import math
import random
name = input("name :")
print(name)
print(type(name))


# to print diffrent data type in a single print statement use , comma

z=97

print(name , z)

# none is similar to null
nothing = None 

# this ord inbuild function print ascii value number
ch = "a"
print(ord(ch))

# this ascii function print character corsponded to number

print(chr(z))


# strings are immutable
# string has indexing feature

name = "ramotar malhotara"
print(name[2:7])

print(name.upper())

str2 = name.capitalize()

# strings methods

# split
# replace 

# https://www.w3schools.com/python/ref_string_format.asp

print("the {} jumped over the {}".format("cow","fence"))

st3 = "ria_mia_kia_lia_diya"

spl = st3.split("_", 3)
print(spl)



pi=3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(pow(pi,2))
print(math.sqrt(pi))



x = random.randint(1,6)

mylist = ["rock" , "paper" , "scissor"]

z = random.choice(mylist)
print(z)