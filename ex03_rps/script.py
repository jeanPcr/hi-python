import random

def checkUserInput(value):
    user_turn = int(value)
    while user_turn>3 or user_turn <1:
        user_turn = int(input("You have to chose one of these :\n 1 - π\n 2 - π€\n 3 - βοΈ\n \n : "))
    return (user_turn)
    
def start():
    symbole = ["π","π€","βοΈ"]
    print ("π₯ Welcome to the Rock, Paper, Scissors Game π₯".center(80,'*'))
    user_turn = int(input("Play :\n\n 1 - π\n 2 - π€\n 3 - βοΈ\n \n : "))
    user_turn = checkUserInput(user_turn)
    pc_turn = random.randint(1,3)
    
    while user_turn == pc_turn :
        print("π― EQUALITY!".center(80,'*')) 
        print("==> π€: %s"%symbole[pc_turn-1])
        print("==> You: %s"%symbole[user_turn-1])
        user_turn = int(input("Play again :\n 1 - π\n 2 - π€\n 3 - βοΈ\n \n : "))
        user_turn=checkUserInput(user_turn)
        pc_turn = random.randint(1,3)
   

    if user_turn == 1 and pc_turn == 2:
        print("YOU LOSTπ".center(80,'*')) 
    elif user_turn == 1 and pc_turn == 3:
        print("YOU WINβ¨".center(80,'*')) 
    elif user_turn == 2 and pc_turn == 1:
        print("YOU WINβ¨".center(80,'*')) 
    elif user_turn == 2 and pc_turn == 3:
        print("YOU LOSTπ".center(80,'*')) 
    elif user_turn == 3 and pc_turn == 1:
        print("YOU LOSTπ".center(80,'*')) 
    elif user_turn == 3 and pc_turn == 2:
        print("YOU WINβ¨".center(80,'*')) 

    print("==> π€: %s"%symbole[pc_turn-1])
    print("==> You: %s"%symbole[user_turn-1])


start()