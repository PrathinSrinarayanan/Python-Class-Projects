from random import randint
number_roll = int(input("How many dice to roll?"))
for _ in range(number_roll):
    die_face = randint(1,6) 
    if die_face == 1: 
        print("-------------")
        print("|           |")
        print("|     x     |")
        print("|           |")
        print("-------------") # If die_face is 1, then it tells the computer to print all the pictures
    if die_face == 2: 
        print("-------------")
        print("| x         |")
        print("|           |")
        print("|         x |")
        print("-------------")
    if die_face == 3: 
        print("-------------")
        print("| x         |")
        print("|     x     |")
        print("|         x |")
        print("-------------")
    if die_face == 4: 
        print("-------------")
        print("| x       x |")
        print("|           |")
        print("| x       x |")
        print("-------------")
    if die_face == 5: 
        print("-------------")
        print("| x       x |")
        print("|     x     |")
        print("| x       x |")
        print("-------------")
    if die_face == 6: 
        print("--------------")
        print("| x        x |")
        print("| x        x |")
        print("| x        x |")
        print("--------------")
