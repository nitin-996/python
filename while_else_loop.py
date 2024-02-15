p = 1234
c = 0
while c != 3:
    c = c + 1
    pin = int(input("enter the pin"))
    if pin == p:
        print("trasaction successful")
    else:
        print("incorrect pin")
else:
    print("card blocked")
