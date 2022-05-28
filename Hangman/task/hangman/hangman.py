# Write your code here
import random
from operator import contains

won = 0
lost = 0
print("H A N G M A N")
print(f"#8 attempts")


def menu():
    action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if action == "play":
        play()
        menu()
    elif action == "results":
        print(f'You won: {won} times')
        print(f'You lost: {lost} times')
        menu()


def play():
    att = 8
    answers = ['python', 'java', 'swift', 'javascript']
    correct_answer = answers[random.randrange(0, len(answers))]
    correct_answer_hidden = "-" * len(correct_answer)
    answer_set = set(correct_answer)
    correct_answer_list = list(correct_answer)
    correct_answer_hidden_list = list(correct_answer_hidden)
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    guess = set()

    while att > 0:
        if contains(''.join(correct_answer_hidden_list), "-"):
            print(''.join(correct_answer_hidden_list))
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('Please, input a single letter.')
            elif letter not in english_alphabet:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in answer_set:
                if contains(''.join(correct_answer_hidden_list), letter):
                    print("You've already guessed this letter.")
                else:
                    for i in range(0, len(correct_answer_list)):
                        if correct_answer_list[i] == letter:
                            correct_answer_hidden_list[i] = correct_answer_list[i]
            elif letter in guess:
                att -= 1
                print("You've already guessed this letter.")
            else:
                guess.add(letter)
                att -= 1
                print("That letter doesn't appear in the word.")
            print(f"#{att} attempts")
        else:
            print(f"You guessed the word {correct_answer}!")
            print("You survived!")
            global won
            won += 1
            break
    else:
        print("You lost!")
        global lost
        lost += 1


menu()
