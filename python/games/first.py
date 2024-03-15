import random

choices = ["rock","paper","scissor"]

computer = random.choice(choices)


player = None


while player not in choices:
   player = input("what is your choice: rock, paper or scissor ?").lower()
   print("computer output :", computer)
   print("player output : ", player)

if (player == computer):
      print("match draw")
   


   





