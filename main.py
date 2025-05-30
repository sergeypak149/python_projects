import random

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
comp_choice = [rock, paper, scissors]
a = random.randint(0, 2)

if user_choice == "0" and a == 0:
    print("Your choice:")
    print(rock)
    print("Computer's choice:")
    print(rock)
    print("Draw")

if user_choice == "0" and a == 1:
    print("Your choice:")
    print(rock)
    print("Computer's choice:")
    print(paper)
    print("You lose")

if user_choice == "0" and a == 2:
    print("Your choice:")
    print(rock)
    print("Computer's choice:")
    print(scissors)
    print("You win")

if user_choice == "1" and a == 0:
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(rock)
    print("You win")

if user_choice == "1" and a == 1:
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(paper)
    print("Draw")

if user_choice == "1" and a == 2:
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(scissors)
    print("You lose")

if user_choice == "2" and a == 0:
    print("Your choice:")
    print(scissors)
    print("Computer's choice:")
    print(rock)
    print("You lose")

if user_choice == "2" and a == 1:
    print("Your choice:")
    print(scissors)
    print("Computer's choice:")
    print(paper)
    print("You win")

if user_choice == "2" and a == 2:
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(scissors)
    print("You lose")



