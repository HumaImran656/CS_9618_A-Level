import random

user_wins = 0
computer_wins = 0

throw_options = ["rock", "paper", "scissors"]

while True:
    user_input = input("What would you throw, rock, paper or scissors?(or press Q to quit): ").lower()
    if user_input == "q":
        break

    if user_input not in throw_options:
        print("sorry you made a typo")
        continue

    random_number = random.randint(0, 2)
    # rock --> 1\\paper --> 2\\scissors -->3\\
    # This was added to make the program perfect 50 lines of code
    computer_pick = throw_options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Wow! looks like you and the computer made the same throw! No point awarded to anyone!")

    elif user_input == "paper" and computer_pick == "paper":
        print("Wow! looks like you and the computer made the same throw! No point awarded to anyone!")

    elif user_input == "rock" and computer_pick == "rock":
        print("Wow! looks like you and the computer made the same throw! No point awarded to anyone!")

    else:
        print("You lose!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
