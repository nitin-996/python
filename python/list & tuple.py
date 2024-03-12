# list is mutable

list = [1,3,5,6,10,7,8,]
list_2=[99,88,77,66,55,44]

list.extend(list_2) # concat the list.
list.append(4)  # add element at the end of the list.

list[1:4]   # slicing
list.sort() # it sort in ascending order
list.sort(reverse=True) # it sort in descending order

# list.reverse()

list.insert(0,50)  # insert at specific index
list.pop(2) # remove value at index 2 if index no is not mention then it will remove last element in list.

list.remove(5)  # here we have we to mention which value need to be removed 

# list comprehention
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

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
tupcopy = (55,) # initiate tuple
tup = (5, 6, 9)

print(type(mock))      
print(type(tup))       
print(type(tupcopy))   


if 5 in tup:
    print( 5, "is present in tuple" )

# unpacking of tuple
    
    no1 ,no2, no3 = tup
print(no1)
print(no2)
rev_tup=reversed(tup)

print(*rev_tup)       