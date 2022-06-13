import random

def game_rules():
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
game_rules()
def gaming_function() :
    

    #a list to store all possible options:
    choices = ["r", "p" , "s"]

    #ask the user to pick an option between "R", "P" or "S"
    print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n ")

    choice = input("Your turn: ").lower()

    
    #search if choice is in available in the choices list
    def search(list, choice):
        for i in range(len(list)):
            if list[i] == choice:
                return True
        return False
    while search(choices, choice) == False:
        choice = input("enter valid input: ").lower()

    if choice == "r":
        choice_name = 'Rock'
    elif choice == "p":
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    print("Your choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # Computer randomly chooses any option
    comp_choice = random.choice(choices)


    if comp_choice == "r":
        comp_choice_name = 'Rock'
    elif comp_choice == "p":
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name)
    
    print(choice_name + " V/s " + comp_choice_name)

    if choice == comp_choice:
        print("Draw=> ", end = "")
        result = "Draw"


    elif ((choice == "r" and comp_choice == 'p') or (choice == 'p' and comp_choice == 'r')):
        print("paper wins => ", end = "")
        result = "Paper"
    elif ((choice == "s" and comp_choice == 'r') or (choice == 'r' and comp_choice == 's')):
        print("rock wins => ", end = "")
        result = "Rock"
    else: 
        print("scissor wins => ", end = "")
        result = "Scissor"

    def announce_winner(result) :
        if result == "Draw":
            print('It is a tie, so close!! try again' )
            gaming_function()
        elif result == choice_name:
            print("You win!! Iwolokan")
        else:
            print ("Opps!! Computer wins")

    announce_winner(result)

gaming_function()