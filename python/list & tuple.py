# sort() method = used with lists
# sorted() function = used with iterable 

students = [("squidward", "F", 25),
            ("sandy", "A", 95),
            ("patrick", "D", 40),
            ("mr.krabs", "B", 80 )]

grade = lambda student: student[1]
students.sort(key=grade)  # Sort the list by the second column (grade)

# https://www.geeksforgeeks.org/sort-in-python/

for student in students:
    print(student)


# map( =  applies a function to each item in an iterable(list,tuple,etc))

# map(function,iterable)  basically map function takes function and iterable , on this iterable function works.
    


# Define a function to apply a 5% discount to a price
def apply_discount(price):
    return price * 0.95

# Create a list of tuples with store items and their original prices
items_with_prices = [('Rice', 80), ('Wheat', 45), ('Sugar', 40), ('Milk', 50), ('Eggs', 60)]

# Use the map function to apply the discount to the prices
# The map function returns an iterator, so we convert it to a list of tuples
discounted_items = list(map(lambda item: (item[0], apply_discount(item[1])), items_with_prices))

# Print the list of items with discounted prices
print(discounted_items)


# filter() function
# Syntax: The filter() method has the following syntax:
# filter(function, sequence)

# function: A function that tests whether each element of the sequence is true or not.
# sequence: The sequence (such as lists, sets, tuples, or other iterable containers) that needs to be filtered.
# Returns: An iterator containing the filtered elements.



# reduce() 


# list is mutable

list_1 = [1,3,5,6,10,7,8,]
list_2=[99,88,77,66,55,44]

list_1.extend(list_2) # concat the list.
list_1.append(4)  # add element at the end of the list.

list_1[1:4]   # slicing
list_1.sort() # it sort in ascending order
list_1.sort(reverse=True) # it sort in descending order

# list.reverse()

list_1.insert(0,50)  # insert at specific index
list_1.pop(2) # remove value at index 2 if index no is not mention then it will remove last element in list.

list_1.remove(5)  # here we have we to mention which value need to be removed 
print(list_1)
# list comprehention
# a way to create a new list wioth less syntax


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

students = [45, 60, 67, 98, 89, 54, 35, 43, 56, 0, 11]

#pass_marks = list(filter(lambda x: x > 60, students)) 

pass_marks= [i for i in students if i >=60]

pass_marks= [i if 1 >= 60 else "failed" for i in students ]

print(pass_marks)







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