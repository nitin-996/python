b =5
c = 24

print(int(c / b))
print(c / b)

# string is imutable

op = ''' this 'is' a still "op" '''
print(len(op))

# in python string gets indexing like array 



op_1 = op[1:5]
print(op_1)

# identity operators (these check object type)
x=5
y=5

print(x is y)
print(x is not y)

# memnership operators (these check if value is present in list)

fruits = ["banana","manago","orange","apple"]

print("banana" in fruits)
print("pineapple" not in fruits)

