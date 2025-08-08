import random

lower_limit = int(input("please input the lower limit"))
upper_limit = int(input("please input the upper limit"))


num = random.randint(lower_limit,upper_limit)
ch = 10 # total chances a user get to guess the nmber

print(f"total changes to guess the number is {ch}")
# gc=guess_counter
gc = 0

while gc < ch:
     
    gc += 1 
   

    rem = (ch - gc)
     

    

    user_input = int(input("please guess the number: "))
    
    if (user_input < lower_limit or user_input > upper_limit):
        print("you have enter incorrect range")
        break

    print(f"remaining changes {rem}")
    
    if (user_input == num):
        print("you have guess it correct")
        break
    elif (rem == gc ):
        print(f"you have lost") 
        

     
