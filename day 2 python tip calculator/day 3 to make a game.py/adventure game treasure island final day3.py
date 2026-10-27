print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Hi" +" " + input("what is your name: "))
print("welcome to treasure island.")
print("your mission is to find the treasure!!" )



print('you are at a river cross road, where do you want to go ? "left" or "right" ')
choice_1 = input('what move do you wish to make ? "left" or "right"\n ').lower()
if choice_1 == "left" :
    print('##. you have successfully gotten to the beach where the treasure is located ,you are to get to the other side of the island through the beach to get your treasure."swim" or "wait for a boat." !')
    choice_2 = input('what move do you wish to make? "swim" or "wait"\n ').lower()

    if choice_2 == "wait" :
        print('##. you have successfully gotten to the other side of the island, you are to open a door with different colours:("red" , "blue" , "yellow") ')
        choice_3 = input('what colour of door do wish to open ? "red","blue","yellow".\n ').lower()

        if choice_3 == "yellow" :
            print("##. you got the treasure,hurray you are a gem!!! ")
        elif choice_3 == "blue" :
            print("##. you fell into a room filled with acid, game over!!")
        elif choice_3 == "red" :
            print("##. you fell into a den of lions, game over!! ")
        else :
            print("##. you chose a door that does not exit. game over!!")
    else :
        print("##. you got eaten by crocodies, game over!! ")
else :
    print("##. you fell into a pot hole , game over!! ")





input("\npress enter to exit...")

# print("you are at a river cross road, where do you want to go ? left or right." )
# input('where do you want to go? "left" or "right".')
# if "left" :
#     print("you have successfully gotten to the beach ")
#     print("you have gotten to the river, do wish to swim now to get to the treasure quickly? or wait for a boat. ")
#     input('do you want to "swim" or "wait" ?')
#     if "swim" :
#         print("sorry you got eaten by crocodiles,game over!!! ")
    

#         print("you have gotten to a door, and behind this lies something great:(THE TREASURE!!)  ")
#         print("now you are to choose the right colour to the door; if a wrong colour to the door is chosen GAME OVER!!!  ")
#         print("you are to choose between red, blue or yellow")
#         input("what colour do you wish to pick;red, blue or yellow ? ")
#         if "yellow" : 
#             print("congratulations you have won your treasure!!! ")
#         else :
#             print("sorry, you opened the wrong door; GAME OVER!!! ")
#     else :
#          print("you have successfully gotten to a door. ")
# else :
#     print("sorry you fell into a pot hole, game over !!! ")
