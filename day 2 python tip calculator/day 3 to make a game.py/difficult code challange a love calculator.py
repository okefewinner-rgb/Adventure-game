# name = "JOHN"
# print(name.lower())

name_1 = input("what is your name :\n ")
name_2 = input("what is your name :\n ")

lower_case_names = ((name_1) + (name_2)).lower()
# print(lower_case_names)
count_true = lower_case_names.count("t") +  lower_case_names.count("r") + lower_case_names.count("u") + lower_case_names.count("e")
count_love = lower_case_names.count("l") + lower_case_names.count("o") + lower_case_names.count("v") + lower_case_names.count("e")
# print(count_true)
# print(count_love)
 

final_love_score_verdict = int(str(count_true) + str(count_love))

if final_love_score_verdict < 10 or final_love_score_verdict > 90 :
    print(f"your score is {final_love_score_verdict},you go together like coke and mentos.")


elif final_love_score_verdict <= 50 and final_love_score_verdict >= 40 :
    print(f"your score is {final_love_score_verdict},you are alright together.")

else :     
    print(f"your score is {final_love_score_verdict}.")


input("\npress enter to exit...")