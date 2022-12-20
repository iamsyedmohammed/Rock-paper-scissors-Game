import random
plater=0
bot=0
print("This is a Game of Rock,Paper,Scissor")
number=int(input("How times you Want to Play:\n"))
option=("Rock","Paper","Scissor")
print(option)
for i in range(number):
    computer=random.choice(option)
    user=input("Enter any one of the option:\n")
    print(computer)
    if computer==user:
        print(f"its is a tie {user} & {computer}")
    elif(user=="Rock" and computer=="Paper")or(user=="Paper" and computer=="Rock") or (user=="Scissor" and computer=="Paper"):
        plater+=1
        print(f"You choose {user} & computer choose {computer}\n So You Won:)")
    elif(user=="Scissor" and computer=="Rock") or (user=="Paper" and computer=="Scissor") or (user=="Rock" and computer=="Scissor"):
        bot+=1
        print(f"You have lost the game you choose {user} computer choose {computer} :(")
if plater>bot:
    print("User Have Won")
elif plater==bot:
    print("It is Tie Between You & Bot")
else:
    print("Bot Have Won")

