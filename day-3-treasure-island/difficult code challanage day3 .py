year= int(input("which year do you want to check? "))   
suggestion_1 = year % 4
suggestion_2 = year % 100
suggestion_3 = year % 400
if suggestion_1 == 0 : 
    if suggestion_2 == 0 :
        if suggestion_3 == 0 :
            print(f"{year},is a leap year")
        else:
            print(f"{year},is not a leap year.")
    else:        
        print(f"{year},is a leap year.")
else:
    print(f"{year},is not a leap year.")

input("\npress Enter to exit....")
# year = int(input("Enter year"))
# if (year % 4 == 0 and year % 400 == 0 and year % 100 != 0):
#     print("This year is a leap year")
# else:
#     print("This is not leap year")