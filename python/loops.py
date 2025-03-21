

  # second question for row-cloumn

# for i in range(1,n+1):
#     for j in range(1,i+1):
#       print(j,end="")
#     print()   


def fizz_buzz(item):
    if (item%3 and item%5) == 0:
        return "fizz_buzz" 
    elif (item%3) == 0:
        return "fizz"
    elif (item%5) == 0:
        return "buzz"
    else: 
        return item


print(fizz_buzz(7))