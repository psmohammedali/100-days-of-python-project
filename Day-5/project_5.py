import random

print("Password Generator")
pass_length = int(input("What should be the password length 7 - 15: "))
no_of_symbols = int(input("Number of symbols: "))
no_of_numbers = int(input("How many numbers you need in your password: "))


char = ["sym", "num", 'alpha']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
alphabets = []
for i in range(65, 90 + 1):
    alphabets.append(chr(i))
for i in range(97, 122 + 1):
    alphabets.append(chr(i))


final_password = ""


for i in range(pass_length):
    chose_char = random.choice(char)
    if chose_char == "sym" and no_of_symbols > 0:
        final_password += random.choice(symbols)
        no_of_symbols -= 1
    elif chose_char == "num" and no_of_numbers > 0:
        final_password += str(random.randint(0, 9))
        no_of_numbers -= 1
    else:
        final_password += random.choice(alphabets)
print(final_password)
