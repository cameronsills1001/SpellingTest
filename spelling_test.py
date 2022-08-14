__author__ = 'cameron'
#main function of the program

from Phrase_Maker import *
from Player import *
from Read_Write import *
import os

phrase = Phrase_Maker()
player = Player()
scribe = Read_Write()

print("My name is PEARL. I'm going to help you with your spelling homework.")
player.phrase_player("fixed_phrases/greeting.mp3")

def menu():
    print("Please choose from the following choices.")
    print("Create (N)ew list, (T)est, (V)iew the weeks points and words, or e(X)it.")
    menu_choice = input("Please enter N, T, V, or X: ")
    if menu_choice.lower() == 'n':
        new_list()
    elif menu_choice.lower() == 't':
        run_test()
    elif menu_choice.lower() == 'x':
        print("Thank you for practicing your spelling words")
    elif menu_choice.lower() == 'v':
        view_info()
    else:
        print("I didn't understand what you were trying to do.")
        menu()

def new_list():
    print("Creating a new list will erase any old list and reset the weekly points to 0")
    cont = input("Do you want to continue? Y or N  ")
    if cont.lower() == 'n':
        menu()
    elif cont.lower() != 'y' and cont.lower() != 'n':
        print("I'm sorry, I didn't understand. ")
        menu()
    #intial set up for the new list and setting points back to zero
    os.system("rm user_speech_files/*.mp3")
    word_list = []
    points = 0
    print("Please enter this weeks spelling words.")
    print("Enter '--done' when you are finished")

    #loop to create the list from user input
    while True:
        word = input("Enter your word: ")
        if word == '--done':
            break
        else:
            word_list.append(word)
    #writing the list and points to file
    scribe.write_list(word_list)
    scribe.set_points(points)

    #taking list and making speech files from them
    for i in word_list:
        phrase.make_phrase(i, "user_speech_files/%s" %i)

    #end and go back to menu
    menu()


def run_test():
    #getting info from file and setting num_correct to zero
    word_list = scribe.read_list()
    points = scribe.get_points()
    num_correct = 0

    print("Get ready for your quiz! \n\n\n")

    for i in word_list:
        #asking the question
        print("Your next word is... ")
        player.phrase_player("fixed_phrases/next_word.mp3")
        player.phrase_player("user_speech_files/%s.mp3" %i)

        #user attempt to spell the word correctly
        user_attempt = input("Enter your word here: ")
        if user_attempt == i:
            print("\nYou are correct!")
            player.phrase_player("fixed_phrases/correct.mp3")
            num_correct += 1
        else:
            print("\nI'm sorry, that is not correct.")
            player.phrase_player("fixed_phrases/incorrect.mp3")

    #finish the test and tally up points
    points += num_correct
    print("\nGood job. You got %s correct\n" %num_correct)
    scribe.set_points(points)

    #go back to menu
    menu()

def view_info():
    points = scribe.get_points()
    words = scribe.read_list()
    print("\nThis week you have earned %s points.\n" %points)
    print("The words for this week are:")
    for i in words:
        print("%s" % i)
    print("")
    menu()

menu()







