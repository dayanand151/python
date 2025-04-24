import random 

number = random.randint(1,100)
while True:
    try:
        gnumber = int(input("Guess the number between 1 and 100 : "))
        if gnumber > number:
            print("Too high")
        elif gnumber < number:
            print("too low")
        elif gnumber == number:
            print("Guessed the right number ")
            break       
    except ValueError as e:
        print("Enter the valid number")
    
    


