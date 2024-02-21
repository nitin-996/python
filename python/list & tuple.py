# list is mutable

list = [1,3,5,6,10,7,8,]

list.append(4)

list[1:4]   # slicing
list.sort()

# list.reverse()

list.insert(0,50)  # insert at specific index
list.pop(2) # remove value at index 2

list.remove(5)  # here we have we to mention which value need to be removed 

print(list)


# checking if a list is palindrome or not

ln = [1,2,3,2,1]

ln_cop = ln.copy()

ln_cop.reverse()

if ln_cop == ln:
    print("its a palindrome")


# tuple is imutable
# if we have single value in tuple then we have to write ,(comma) at the end.

mock = (55)
tupcopy = (55,)
tup = (5, 6, 9, 7, 8, 6, 3)

print(type(mock))      
print(type(tup))       
print(type(tupcopy))   


