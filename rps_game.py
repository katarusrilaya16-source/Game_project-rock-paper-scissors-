import random


user_score = 0
computer_score = 0


choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors Game!")
print("Type 'exit' to quit the game.\n")

while True:

    
    user = input("Enter rock, paper, or scissors: ").lower()

    
    if user == "exit":
        print("\n👋 Game Ended")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break

    
    if user not in choices:
        print("❌ Invalid Choice! Try again.\n")
        continue

    
    computer = random.choice(choices)

    print(f"🤖 Computer chose: {computer}")

   
    if user == computer:
        print("😐 It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("💻 Computer Wins!")
        computer_score += 1

    
    print(f"📊 Score -> You: {user_score} | Computer: {computer_score}\n")