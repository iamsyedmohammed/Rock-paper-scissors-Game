import random
import time
player=0
bot=0
player_score=0
bot_score=0
print("This is a Game of Rock,Paper,Scissor")
number=int(input("How times you Want to Play:\n"))
option=("r","p","s")
for i in range(number):
    computer=random.choice(option)
    time.sleep(1)
    user=input("Enter any one of the option \nr for Rock \np for Paper \ns for Scissor:\n")
    print(computer)
    if computer==user:
        time.sleep(1)
        print(f"its is a tie {user} & {computer}")
    elif(user=="r" and computer=="s")or(user=="p" and computer=="r") or (user=="s" and computer=="p"):
        player+=1
        player_score+=1
        time.sleep(1)
        print(f"You choose {user} & computer choose {computer}\nSo You Won 🙂")
    elif(user=="s" and computer=="r") or (user=="p" and computer=="s") or (user=="r" and computer=="p"):
        bot+=1
        bot_score+=1
        time.sleep(1)
        print(f"You  choose {user} & computer choose {computer}\nSo You lost☹")
if player>bot:
    print(f"User Have Won with {player_score} points")
elif player==bot:
    print(f"It is Tie Between You with {player_score} & Bot with {bot_score}")
else:
    print(f"Bot Have Won with {bot_score} points")

