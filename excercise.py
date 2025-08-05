msg= "thi"

if len(msg) > 3:

  new_1 = msg.removeprefix(msg[0])
  add = "xyz"
  first_2_last = msg[0]

  new3 = "".join([add,new_1,add,first_2_last])

  print(new3)

else:
    
    emp_list = []
    i=len(msg)
    # print(i)
    while i<=3:
      i-=1
    #   print(i)
      item = msg[i]
      emp_list.append(item)

      rev = str(emp_list)
      print(rev)

      if i == 0:
         break
      


row_list = [1,2,4,3,55,44,45,43]

for index,value in enumerate(row_list):
   print(f"{index} index {value} value")

   

