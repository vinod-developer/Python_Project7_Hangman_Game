import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

chosen_word_to_array = []
word_list = ["rabbit", "mouse", "elephant"]

# chosen_word = random.choice(word_list)
chosen_word = "mouse"
chosen_word_in_lower = chosen_word.lower()
print(chosen_word_in_lower)
guessed_word = ['m', 'o', 'u', 's', 'e']

blank_string = ""
blank_string_to_array = []
chosen_word_to_array = chosen_word_in_lower
for ch in range(0, len(chosen_word_in_lower)):
    blank_string += "_"
print("blank string" + blank_string)
blank_string_to_array = blank_string
print(blank_string_to_array)

char_value = ''


def is_letter_in_the_word(char_value_arg, blank_string_arg, chosen_word_arg):
    for i in chosen_word_arg:
        print(" looping var "+i)
        print(f"char value arg is {char_value_arg} ")
        print(i == str(char_value_arg))
        if i == str(char_value_arg):
            num = chosen_word_arg.index(i)
            blank_string_arg = blank_string_arg[:num] + char_value_arg
            print(f"in if loop {blank_string_arg}")
    print(blank_string_arg)


for g in range(0, len(chosen_word_in_lower)):

    print(chosen_word_in_lower[g])
    is_letter_in_the_word(chosen_word_in_lower[g], blank_string_to_array, chosen_word_to_array)
    print("--------->")
