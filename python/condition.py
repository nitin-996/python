num1 = int(input("type the number : "))
name = input("type the name : ")

if ((num1 == 1 or num1 == 2) and name == "ns"):
    print("fee is 100")
elif(num1 == 3 or num1 == 4 or name == "ms"):
    print("fee is 200")    
else:
    print("no one")    



# ternary opeprator
    
food = "chap"
eat = "yes" if food == "paneer" else "no"
print(eat)

# clever if 

# <var> = ( true_val, false_val)[<condotion>]

age = 19
age = ("yes", "no") [age >=18]

