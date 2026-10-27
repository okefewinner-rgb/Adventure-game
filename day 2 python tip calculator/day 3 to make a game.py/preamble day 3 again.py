print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoster!")
    age=int(input("what is your age? "))
    if age < 12 :
        bill = 5 
        print("child ticket are $5. ")
    elif age<= 18:
        bill = 7
        print("youth tickets are $7.")
    elif age >= 45 and age <= 55 :
        bill = 0
        print("your ride is free!" )
    else:
        bill = 12
        print("Adult tickets are $12.")

    picture = input("Do you want pictures ? yes or no ")    
    if picture == "yes" :
           total_bill = bill + 3
    print(f"your total bill is ${total_bill}")
else:
    print("sorry,you have to grow taller before you can ride.")


input("\npress Enter to exit...")