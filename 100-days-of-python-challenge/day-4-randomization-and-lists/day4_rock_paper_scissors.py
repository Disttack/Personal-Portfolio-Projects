import random

random_int = random.randint(a=0,b=2)
choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: ")

if choice == "0":
    print('''Your choice is:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
elif choice == "1":
    print('''Your choice is:
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
          ''')
elif choice == "2":
    print('''Your choice is:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''')
else:
    print("Please choose a valid number.")

if random_int == 0:
    print('''The computer chooses:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          ''')
elif random_int == 1:
    print('''The computer chooses:
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
          ''')
elif random_int == 2:
    print('''The computer chooses:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''')

if choice == "0" and random_int == 0:
    print("Tie!")
elif choice == "0" and random_int == 1:
    print("You lose!")
elif choice == "0" and random_int == 2:
    print("You win!")

if choice == "1" and random_int == 0:
    print("You win!")
elif choice == "1" and random_int == 1:
    print("Tie!")
elif choice == "1" and random_int == 2:
    print("You lose!")

if choice == "2" and random_int == 0:
    print("You lose!")
elif choice == "2" and random_int == 1:
    print("You Win!")
elif choice == "2" and random_int == 2:
    print("Tie")