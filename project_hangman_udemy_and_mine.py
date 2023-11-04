import random

word_list = ["apple", "banana", "orange"]

chosen_word = random.choice(word_list)
chosen_word_list = []
chosen_word_list = chosen_word
print(chosen_word_list)

display = []
len_chosen_word = len(chosen_word)
for i in range(len_chosen_word):
    display += '_'
print(display)
count = 0
for i in range(len_chosen_word +1):
    if display != list(chosen_word):
        print(f"listof chosen word {chosen_word}")
        guessed_letter = input("pls enter your guess")
        for position in range(len_chosen_word):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = letter
        print(f"---> {display}")
    elif display == list(chosen_word):
        print("you won")
        break
    else:
        print("you lose")
        break

