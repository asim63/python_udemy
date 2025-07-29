print("Welcome to Tresure Island.\n Your mission is to find the treasure.")

dir = input("Where do you wanna go? Left or Right (input L or R): ")

if(dir == "L"):
    action = input("There is a flood!. Do you wanna swim or wait? (input S or W ): ")
    if(action == "W"):
        door = input("There are three doors. Red, Blue and Yellow. Which do you choose? (Input R or B or Y): ")
        if(door == "Y"):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over")
else:
    print("Game Over")

