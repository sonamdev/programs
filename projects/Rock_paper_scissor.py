import random
human = input("Select Rock, Paper, or Scissor :").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()

print("computer selected: ", computer)

if human == "rock" and computer == "paper":
    print("computer Won")
elif human == "paper" and computer== "scissor":
    print("computer Won")
elif human == "scissor" and computer == "rock":
    print("computer Won")
elif human == computer:
    print("Tie")
else:
    print("human Won")