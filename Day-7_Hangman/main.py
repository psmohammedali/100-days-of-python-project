# Customized modules
import heading
import hangman_ascii
import word_list
# Pre-defined Modules
import random

heading.project_heading()

current_word = word_list.words[random.randrange(len(word_list.words))]
current_set = set(current_word)
# print(current_set)
print("Let's start the GAME !!!!")
current_state = 0
final_stage_number = len(hangman_ascii.hangman_stages) - 1

user_ans = ""
user_set = set()

for i in range(len(current_word)):
    print("_",end="")
print()

while current_state <= final_stage_number:
    user_input = input("Enter a Letter: ").lower()
    if user_input in current_set:
        user_set.add(user_input)
        for i in current_word:
            if i in user_set:
                print(i, end="")
            else:
                print("_", end="")
        print()
        if len(user_set) == len(current_set):
            print("YOU WON, CONGRATULATIONS !!!!")
            break
    else:
        if current_state == final_stage_number:
            print(hangman_ascii.hangman_stages[current_state])
            print("you Lose")
            print(f"THE CORRECT ANSWER IS {current_word.upper()}")
            break
        print(hangman_ascii.hangman_stages[current_state])
        current_state = current_state + 1
