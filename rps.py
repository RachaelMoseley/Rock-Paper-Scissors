sentence = "Hello, welcome to our rock, paper, scissors game."
print(sentence)

name1 = "r" + "rock"
name2 = "p" + "paper"
name3 = "s" + "scissors"

print("Choose your variable: ")
x = input()
print('your variable is ' + x + ".")

if name1 == "rock" + "scissors":
    print('Player 1 wins and PLayer 2 loses!')
else:
    print('You Player 1 lost and Player 2 wins!')
#idk
if name2 > "paper" + "rock":
    print("Player 1 wins and PLayer 2 loses!")
else: 
    print("Player 2 wins and PLayer 1 wins!")

if name3 == "scissors" + "Paper":
    print("Player 1 wins and PLayer 2 loses!")
else:
    print("Player 1 loses and PLayer 1 wins!")