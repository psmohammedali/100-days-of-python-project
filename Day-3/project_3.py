#  .,::::..
#                       ';''':';:.
#                        (o  o |;
#                        | <   );
#                        \ --' |
#                      ___'-.  |____
#                    .'    -  -     `'.
#                  ,'_      :          '.
#                 : [_]  ,  :  ,         :
#                 : :  ) --' '--- :`'... '.
#                 :   / \:: : :: /    :   :
#                  '''  |'' , ''|     : .'
#                       :===u==='.   (,,;
#                      /          :__|__|__
#                      :    __    |/       |
#                      :    ::    ||       |
#                      :    : :   ||       |
#                      '.   :  :  ''-------'
#                      :    :  :    :
#                  snd :    :  :    :
#                      :____:  :____:
#                    .-='  \    ( ==\
#                   (____,_/     \   \
#                                 '--'

print("Welcome to Treasure Island \nYour Mission is to find the treasure")
direct = input("You wanna take right or left: ")
if direct.lower() == "left":
    print("You reached the river side, you need to swim or wait for the boat")
    action = input("Swim or wait: ")
    if action.lower() == "wait":
        print("You reached to the door section. There are three doors: Blue, Yellow, Red")
        door = input("which to door to enter: ").lower()
        if door == 'red':
            print("Burnt with fire\nGame Over")
        elif door == "blue":
            print("Eaten by beasts\nGame Over")
        elif door == "yellow":
            print("YOU WOM!!! CONGRATULATIONS...")
        else:
            print("Game Over")

    else:
        print("Attacked by trout while swimming")
        print('Game Over')


else:
    print("you have fell into the Hole")
    print("Game Over")
