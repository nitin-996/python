
# default parameter function

a = 5
b = 10

def fun1(a,b=3):
    print(a,b)

fun1(a,b)


def many_no(*args):
    print(args)

many_no(25,65,98,78,69)
 

def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x , "is", y)

studentinfo(name="urvi" , age=22, city="delhi")     


# n=int(input())

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * fact(n-1)
        print(result)
        return result

print(fact(5))


# higher order function = a function that either
 # 1. accepts a function as an argument or 
# 2. returns a function  (in python, functions are also treated as objects)


def loud(text):
    return text.upper()


def low(text):
    return text.lower()

def write(func):
    text = func("Hello")
    return text

print(write(low))    



def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)

print(divide(10))


# lambda function = function written in 1 line using lambda keyword
#                    accepts any number of arguments but only has one expression.


double = lambda x:x *2 

print(double(5))








