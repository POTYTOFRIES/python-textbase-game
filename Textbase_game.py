'''
   A Text base game of life choices as a programming student, choose your own path...
   (I focused on the story line instead of trying out some complicated syntax, most of the syntax I used here are the ones that
   i'm super comfortable na.)

'''
import time

# function to print messages with a 2 second delay
def print_pause(message):
    print(message)
    time.sleep(2)


# function to print messages with a 1 second delay
def print_pause1(message):
    print(message)
    time.sleep(1)

# function to print the letters one by one
def f_print(s):
    for char in s:
        print(char, end="", flush=True)
        time.sleep(0.07)

# ------------------------- ROUTINES -------------------------
f_print("Choices: Programming Student Edition.\n")
print("       ")
player_name = str(input("What is your name? "))

print("Welcome ", player_name,"^^")
print("==============================================================================")
print_pause("\nIn this game you will choose your own path as a programming student.")
print_pause("Your input choices will be '1', '2' and '3' only.")
print("   ")
print_pause("==============================================================================")

# Situation 1 
def sit_1():
    print_pause1("It's 8 am and you have a class at 9 am.")
    print_pause1("\nWhat will you do? ")
    print_pause1("[1]Get up and get ready for the class \n[2]Take a 5 more minutes nap?")
    print("   ")
    choice = input("> ");

    if "1" in choice:
        sit_2()
    elif "2" in choice:
        print_pause("You didn't wake up after 5 minutes and you missed your class...\n")
        game_over("")

# Sit 2

def sit_2():
    print_pause1 ("You attended the class and learned new things, ")
    print_pause1("now your trainer gave an assignment and the deadline is in 2 days.")
    print_pause1 ("\nWill you: \n[1]Do the homework asap to understand it properly. \n[2]Procrastinate and do it the next day. \n[3]You didn't do it at all. ")
    print("   ")
    choice = input("> ");

    if "1" in choice:
        print_pause("You submitted the homework early and gained more knowledge about programming")
        sit_3()
    elif "2" in choice:
        print_pause("You did the assignment but because you rush doing it, you couldn't absorb the information properly.")
        sit_3_2()
    elif "3" in choice:
        print_pause("You didn't do your homework and that made you clueless to your quiz in the next class and failed...")
        game_over("")


# Sit 3

def sit_3():
        print_pause("The next class, your trainer suprised you with a Quiz that will be related to your project and demo.")
        print_pause1("The knowledge you learned from doing the assignment early helped a lot for this Quiz. ")
        f_print(".....\n")
        print_pause("After the quiz, the trainer announced that you Ace the quiz and will now proceed to making your project.")
        f_print("Congratulations!! Clap clap clap...\n\nFew days later...\n")
        print_pause("While making the project, you got stuck with your code, \nyou tried to debug and research on your own but it didn't work...")
        print_pause1("\nWhat will you do? \n[1]Cry and Give up TT \n[2]Ask a trainer for help")
        print("   ")

        choice = input("> ")

        if "2" in choice:
            print_pause1("The trainer you asked, helped you with your coding problems \nand you moved on with your project smoothly. ^^")
            f_print(".....\n")
            sit_4()

        elif "1" in choice:
            print_pause1("You give up programming and drop out, now you're back to 0 without future plans...")
            game_over("")
           
# extra sit for choice 2 in sit 2
def sit_3_2():
        print_pause("The next class, your trainer suprised you with a Quiz that will be related to your project and demo.")
        print_pause("And since you couldn't properly understand the assignment, you had a hard time with the Quiz and couldn't finish it on time.")
        f_print(".....\n")
        print_pause("After the quiz, the trainer told you that you failed and won't be able to proceed with the project...")
        print("  ")
        game_over("")


# Sit 4 
def sit_4():
        print_pause1("After finishing your project, you have 3 more days before your Demo day.")
        print_pause1("Now you are very nervous because presenting is not your biggest skill \n\nWhat will you do? ")
        print_pause1("[1]Practice your presentation skills. \n[2]Don't attend the Demo day.")
        print("   ")
        choice = input("> ")

        if "1" in choice:
            print_pause1("Because you practiced your presentation skills, \nYou confidently attended the Demo day and got a High Score and an important advice from the Pannelist.")
            f_print(".....\n")
            print_pause1("After your Demo,")
            print_pause("You are now 100% Confident with the path you chose.")
            print_pause("And ready for next challenge that you will have to face.")
            f_print("Congratulations! You are now one step closer to become a Programmer...<3\n\n\n")

            print("===========================================================")
            print_pause("     That's it! Thank you for playing.")
            print("===========================================================\n")
            print("  ")
            game_over("")

        elif "2" in choice:
            print_pause1("Because you didn't attend the demo day, \nyour confidence became Zero and you are doubting if this is the right path for you.")
            print_pause1("And so you gave up and wasted all your efforts...")
            f_print("krazzzzy...\n")
            game_over("")
# START

def start():
    sit_1()

# GAME OVER

def game_over(s):

    print ("Try again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)

# GOING BACK TO THE TOP

start()

