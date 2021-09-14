import random
def hangman():
    words_list=["navgurukul","india","telanga","bangalore","karnataka"]
    word=random.choice(words_list)
    turns=10
    guessmade=" "
    a=list("abcdefghijklmnopqurstuvmxyz")
    while len(word)>0:
        main_word=" " 
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("****your won****")
            break
        print("guesse the words",main_word)
        guess=input("enter the guess word ")
        if guess in a:
            guessmade=guessmade+guess
        else:
            print("enter the valid character")
            # guess=input("enter the guess word")
        if guess  not in word:
            turns=turns-1
            if turns==9:
                print("9 turns are left")
                print("----------------")
                print()
            if turns==8:
                print("8 turns are left")
                print("----------------")
                print("         o      ")
            if turns==7:
                print("7 turns are left")
                print("----------------")
                print("         o      ")
                print("         |      ")
            if turns==6:
                print("6 turns are left")
                print("----------------")
                print("         o      ")
                print("         |      ")
                print("        /       ")
            if turns==5:
                print("5 turns are left")
                print("----------------")
                print("         o      ")
                print("         |      ")
                print("        / \      ")
            if turns==4:
                print("4 turns are left")
                print("----------------")
                print("        \o     ")
                print("         |      ")
                print("        / \     ")
                
            if turns==3:
                print("3 turns are left")
                print("----------------")
                print("        \o/    ")
                print("         |      ")
                print("        / \     ")
                
            if turns==2:
                print("2 turns are left")
                print("----------------")
                print("        \o/ |   ")
                print("         |      ")
                print("        / \     ")
                
            if turns==1:
                print("1 turn is left hangman is on the last breath")
                print("----------------")
                print("        \o/_|   ")
                print("         |      ")
                print("        / \     ")
            if turns==0:
                print("your loose")
                print("the hangman was died")
                print("         o_|    ")
                print("        /|\    ")
                print("        / \     ")
                break
name=input("enter the name")
print("welcome",name)
print("-------")
print("try to guess the word in less than 10 attems")
hangman()
