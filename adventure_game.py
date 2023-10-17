"""
A road crossing adventure game
This is a project work in partial fulfilment for the award of
a nano-degree certificate in Introduction to Programming at
Udacity.

This game simulates crossing a road in a world with no hopes
of the "Walk light" coming up. Everyone always find their own way.

This games brings up the options of approaching a police man, adults
standing nearby or using a pedestrian bridge.

One other feature idea not included is a health bar, which decreases
as they player makes a range of decision. Game ends and player dies
if player fails to cross successfuly before health status reaches <= 0
"""


import random
import time
import textwrap


# Global Variables

count = 0
actions = []
cross_seq = []
choices = [1, 2, 3, 4]
choices_copy = choices.copy()
temp_d = random.randint(1, 10)
positive = ["yes", "y"]
negative = ["no", "n"]


def cprint(message):
    """
    Custom print function to print and delay

    Args:
        message: str to be printed to stdout

    Return:
        message: printed to stdout
        sleep: 2 second
    """
    print(message)
    time.sleep(1)


def cprint2(message):
    """
    Custom print function to print wrapped text and delay

    Args:
        message: str to be printed to stdout

    Return:
        message: printed to stdout
        sleep: 2 second
    """
    wrapped_message = textwrap.wrap(message, 60)
    for line in wrapped_message:
        print(line)
        time.sleep(1)


def intro():
    """
    Storyline
    """

    cprint2("You are 14 years old John, and you needs to run an errand "
            "for your mum across the road. You must choose how to reach "
            "your destination. You may needs some help."
            )
    cprint("")
    cprint2("\"You will also find that help will always be given at Hogwarts "
            "to those who ask for it.\"")
    cprint("- Professor Albus Dumbledore"
           "\nHarry Potter and the Chamber of Secrets")
    print()
    cprint2("***********************************************************")
    cprint2("***********************************************************")
    cprint("")
    while True:
        decision = input("Do you accept to play? (yes/no) ")
        if decision.lower() in positive:
            play()
            break
        elif decision.lower() in negative:
            dont_play()
            break
        else:
            print("That is not a valid response!")


def play():
    """
    Function to play the game and explore the available choices.
    Goodluck!!!
    """
    global count
    if count == 0:
        cprint("\nYou are at the road now. The road is quite busy today.")
    else:
        cprint("\nYou are back at the road now. The road is still quite busy.")
    cprint("There is a policeman sitting in the police car nearby.")
    cprint("Also, there are some adults by the roadside.")
    cprint("You have also sighted pedestrian bridge in the distance.")
    cprint("Now, you must make a decision:\n")
    print("1. Go ahead and cross the road")
    print("2. Approach a nearby adult and ask for help")
    print("3. Approach the policeman, and ask for help")
    print("4. Use the pedestrian bridge about 2km away.")
    print()
    while True:
        try:
            choice = int(input("Make a choice: "))
            count += 1
            if choice == 1:
                if choice in choices:
                    choices.remove(choice)
                    cross()
                else:
                    other_options(choice)
            elif choice == 2:
                if choice in choices:
                    choices.remove(choice)
                    adult()
                else:
                    other_options(choice)
            elif choice == 3:
                if choice in choices:
                    choices.remove(choice)
                    police()
                else:
                    other_options(choice)
            elif choice == 4:
                if choice in choices:
                    choices.remove(choice)
                    bridge()
                else:
                    other_options(choice)
            else:
                print("That's not an option!")
        except ValueError:
            print("That's not an option!")


def dont_play():
    """
    You have chosen not to play the game (again).
    The game will exit now.
    """
    if count == 0:
        cprint("You have decided to return home.")
        cprint("You're being a bad boy.")
        end()
    else:
        cprint("You seems to have gotten all you need.")
        cprint("And you have now decided to go home.")
        end()


def other_options(choice):
    """
    Function to print response when making same choice twice
    Makes the choice available again afterwards.
    """
    cprint("You already tried this option. Try other options.")
    choices.append(choice)


choices = choices_copy


def replay():
    """
    Function to restart game based on player's choice

    Resets all modified global variables
    """
    global actions
    global choices
    global cross_seq
    global count
    actions.clear()
    choices = choices_copy
    cross_seq.clear()
    count = 0
    start()


def cross():
    """
    Function for option selection == "cross"

    You have decided to cross the road alone
    """
    i = 0
    cross_options = [1, 2, 3]
    cross_seq1 = ["left", "right", "left", "go"]
    cross_seq2 = ["right", "left", "right", "go"]
    cross_seq = []
    print()
    cprint("You have decided to cross the road alone.")
    cprint("In order to cross the road, you must complete this correctly.")
    cprint("1. Look left\n2. Look right\n3. Cross now\n")
    while True:
        try:
            cross_action = int(input("Where should you look first? "))
            if cross_action in cross_options and cross_action == 1:
                cprint("Looked left")
                cross_seq.append("left")
                break
            elif cross_action in cross_options and cross_action == 2:
                cprint("Looked right")
                cross_seq.append("right")
                break
            else:
                print("That's not an option!")
        except ValueError:
            print("That's not an option!")
    while len(cross_seq) < 3:
        while True:
            try:
                cross_action = int(input("Where should you look next? "))
                if cross_action in cross_options and cross_action == 1:
                    cprint("Looked left")
                    cross_seq.append("left")
                    break
                elif cross_action in cross_options and cross_action == 2:
                    cprint("Looked right")
                    cross_seq.append("right")
                    break
                else:
                    print("That's not an option!")
            except ValueError:
                print("That's not an option!")

    while True:
        try:
            cross_action = int(input("Select '3' to cross now! "))
            if cross_action in cross_options and cross_action == 3:
                cprint("Crossing...")
                cross_seq.append("go")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("That's not an option!")
    if (cross_seq == cross_seq1) or (cross_seq == cross_seq2):
        cprint("You have been able to cross the road successfully.")
        print()
        cprint2(traffic_crossing)
    else:
        cross_fail()
        while True:
            response = input("Do you want to try again? (yes/no) ")
            if response in positive:
                replay()
                break
            elif response in negative:
                end()
                break
            else:
                print("That's not an option!")

    cross_seq.clear()
    end()


traffic_crossing = "In right-hand traffic, you should look 'left', then \
'right' and then 'left' again before crossing. However, in a left-hand\
 traffic, you should look 'right', then 'left' and then \
'right' again before crossing"


def cross_fail():
    cprint("You didn't take enough caution while crossing the road.")
    cprint("There was an accident.")
    cprint2(traffic_crossing)
    cprint("")
    cross_seq.clear()


def police():
    """
    Function for option selection == "police"

    You will the asking the police man for help
    """
    cprint("You have decided to ask the police for help.")
    availability = random.randint(1, 10)
    if availability >= 5:
        cprint("The police is willing to help.")
        cprint("With the police help, you have "
               "been able to cross the road successfully.")
        end()
    else:
        cprint("The police can't help you now. Please try other options.")
        play()


def adult():
    """
    Function for option selection == "adult"

    You will be approaching an adult for help.
    """
    cprint("You have decided to talk ask an adult for help.")
    genders = ["male", "female"]
    gender = random.choice(genders)
    if gender == "male":
        cprint("Frank is Business man, who has an appoint and is almost late.")
        cprint("Approach with caution.")
        while True:
            talk = input("Do you want to talk to him? (y/n) ")
            if talk.lower() in positive:
                agg = random.randint(1, 10)    # agg: Aggression
                if agg >= 5:
                    cprint("Frank looked angrily at you and "
                           "snapped at you as you asked for help.")
                    print()
                    play()
                else:
                    cprint("Frank has agreed to help you cross the road.")
                    cprint("You've been able to cross the road successfully.")
                    end()
                break
            elif talk.lower() in negative:
                cprint("Do you want to talk to another adult?")
                while True:
                    talk = input("Want to talk to another adult? (y/n) ")
                    if talk.lower() in positive:
                        adult()
                        break
                    elif talk.lower() in negative:
                        play()
                        break
                    else:
                        print("That's not a valid response. Try again.")
                break
            else:
                print("That's not a valid response. Try again.")

    else:
        cprint("Miss Lucy is a pretty lady, who "
               "is about to cross the road as well.")
        cprint("She is willing to help you cross the road as well.")
        cprint("You have been able to cross the road successfully.")
        end()


def bridge():
    """
    Function for option selection == "bridge"
    """
    cprint("You have decided to use the pedestrian bridge.")
    cprint("However, the bridge is 2km away.")
    while True:
        bridge_choice = input("Would you like to continue? (y/n) ")
        if bridge_choice.lower() in positive:
            cprint("You have chosen to use the pedestrian bridge.")
            cprint("Walking.")
            cprint("Walking..")
            cprint("Walking...")
            cprint("Crossing.")
            cprint("You have been able to cross the road successfully.")
            end()
        elif bridge_choice.lower() in negative:
            cprint("The bridge seems to be too far away for you.")
            cprint("You can try other options.")
            play()
        else:
            print("That's not a valid response. Try again.")


def end():
    """
    Ends the adventure game.
    """
    cprint("End of adventure.")
    exit()


def start():
    """
    Starts the adventure game.
    """
    intro()


start()
