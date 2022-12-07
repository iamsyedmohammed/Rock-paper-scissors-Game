import random
option=("Rock","Paper","Scissor")
print(option)
computer=random.choice(option)
user=input("Enter any one of the option:\n")
print(computer)
if computer==user:
    print(f"its is a tie {user} & {computer}")
elif(user=="Rock" and computer=="Paper")or(user=="Paper" and computer=="Rock") or (user=="Scissor" and computer=="Paper"):
   print(f"You choose {user} & computer choose {computer}\n So You Won:)")
elif(user=="Scissor" and computer=="Rock") or (user=="Paper" and computer=="Scissor") or (user=="Rock" and computer=="Scissor"):
 print(f"You have lost the game you choose {user} computer choose {computer} :(")
 