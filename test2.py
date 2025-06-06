from time import sleep

print("Welcome to the treasure island!")
print("Your mission is to find the treasure.")
steps = 0
life_counter = 3
start_game = str(input("Do you wish to start the game? (Y/N): ")).lower()

while life_counter != 0 and start_game == 'y':
    print("Your journey starts here! You wake on a remote beach, all you can see so far is sand.")
    print("What do you do next? Enter A or B!")
    first_choice = str(input("A(Look Around) or B(Screem for Help): ")).lower()
    if first_choice == 'a':
        print("You decided to look around!")
        print("While looking you found a raft, what do you want to do next? Choose A or B!")
        second_choice = str(input("A(Take the raft, and try to leave) or B(Leave the raft where it is)"))
        if second_choice == 'a':
            print("You tried to leave using the raft, under the raft you found a map!")
            print("While swimming, you decide to follow the route on the map.")
            print("When approaching the shore, you notice a bag, what do you want to do next? Choose A or B")
            third_choice = str(input("A(Leave the bag where it is) or B(Pick the bag up)")).lower()
            if third_choice == 'b':
                print("You picked up the bag, it had some food, water, and shovel!")
                print("You eat and drink, which keeps you going!")
                print("Now you are at the place where map indicates you to go! What will you do next? Choose A, B, or C")
                fourth_choice = str(input("A(Leave the place alone, you are too tired), B(You decide to dig using shovel), C(Dig with your hands)")).lower()
                if fourth_choice == 'b':
                    print("You found the treasure, CONGRATS!!!!")
                    break
                elif fourth_choice == 'a':
                    print("You wander into the jungle, sadly you got lost and DIED!")
                    life_counter -= 1
                    sleep(1)
                else:
                    print("Above the treasure you find a very hard sandstone, you can't continue!")
                    print("Night is coming, sadly, it gets too cold! You DIED!")
                    life_counter -= 1
                    sleep(1)
            else:
                print("You don't have any supplies to keep you alive! You DIED!")
                life_counter -= 1
                sleep(1)
        else:
            print("Due to heat and no drinking water around you, you DIED!")
            life_counter -= 1
            sleep(1)
    else:
        print("You tried screaming and shouting, sadly, you attracted wild animals!")
        print("You DIED")
        life_counter -= 1
        sleep(1)