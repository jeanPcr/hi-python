from words import english_words
import random
import re

def choseWord():
    return english_words[random.randint(0,len(english_words))]

def checkCorrectInput(letter):
    while len(letter)>1 or len(re.findall("[a-zA-Z]",letter)) == 0:
       letter = str(input("You must to type one letter to complete the word. Please enter a letter : "))
    return letter.lower()

def word_display(word,right_letters):
        display = ""
        for i in range(len(word)):
            if word[i] in right_letters:
                display = display + word[i]
            else :
                if i == 0 or ( i > 5 and i == len(word)) :
                    display = display + word[i]
                else :
                    if word[i] == "-":
                        display = display + word[i]
                    else :
                        display = display + "_"
                
        print(display.upper().center(80," "))

def wrong_letters_display(wrong_letters):
    display = "Wrong letters : "
    for i in range(len(wrong_letters)):
        display =  display + "|" + wrong_letters[i] 
    print(display)
    print("\n")

def start():
    print ("  🔥 Welcome to the Hangman Game 🔥".center(80,'*'))
    print("\n")
    right_letters = []
    wrong_letters = []
    user_in = ""
    tries = 0

    word_to_find = choseWord()
    letters_to_find = []
    for i in range(len(word_to_find)):
        if word_to_find[i]  not in letters_to_find :
            if word_to_find[i] == "-" :
                continue
            letters_to_find.append(word_to_find[i])
    right_letters.append(word_to_find[0])


    if  len(word_to_find) > 5 :
        right_letters.append(word_to_find[len(word_to_find)-1])

    while len(right_letters) != len(letters_to_find):
        word_display(word_to_find,right_letters)
        print("%s tries left." % ((5-tries)))
        user_in = str(input("Chose a letter🖊️ : \n"))
        user_in = checkCorrectInput(user_in)

        if user_in not in right_letters and user_in in word_to_find and tries != 5:
            right_letters.append(user_in)
            print (" Well played !👍 ".center(80,'*'))
        elif user_in not in word_to_find and tries != 5:
            if user_in not in wrong_letters :
                wrong_letters.append(user_in)
            print (" Missed !🙁 ".center(80,'*'))
            wrong_letters_display(wrong_letters)
            tries = tries +1

        if tries == 5:
            break
    if tries == 0 :
         print (" 😱😱🎉🎉 INCREDIBLE ! You've found at the first attempt. 😱😱🎉🎉 ".center(80,'*') )
    elif tries == 5 :
         print (" ⏰ GAME OVER. You've make to much tries. The word was %s. ".center(80,'*') % (word_to_find)) 
    elif tries != 0 and tries != 5:
         print (" ✨ Congratulations ! You've found the word in %s tries. ✨ ".center(80,'*') % (tries))
         
start()