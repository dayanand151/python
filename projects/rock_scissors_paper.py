import random

letters = ['r', 's', 'p']

while True:
    choice = input("Enter the choice ? r=rock, s=scissors, p=paper \n").lower()
    schoice = random.choice(letters)
    if choice in letters and choice == 'r':
        print(schoice)
        if schoice == 's':
            print("rock will win ")
        elif schoice == 'p':
            print("paper will win")
        else:
            print("Draw")
    elif choice in letters and choice == 's':
        print(schoice)
        if schoice == 'r':
            print("Rock will win ")
        elif schoice == 's':
            print(" Draw ")
        else:
            print("Scissors will Win ")
    elif choice in letters and choice == 'p':
        print(schoice)
        if schoice == 'r':
            print("Paper will win ")
        elif schoice == 's':
            print(" Scissors will win ")
        else:
            print(" Draw ")
    else:
        x= input("Invalid Choice, Do you want to continue ? y\n").lower()
        if x != 'y':
            break


    
