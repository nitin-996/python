
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
