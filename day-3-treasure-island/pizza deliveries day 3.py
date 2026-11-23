print("Hello " + " " + input("what is your name ? "))
print("welcome to pizza Deliveries! ")
print("our menu are: small pizza, large pizza, medium pizza\n" + " "+ "including pepperoni and extra cheese"  )

pizza_choices = input("what pizza do you want ? ")
add_pepperoni= input("Do you want pepperoni ? yes or no. ")
extra_cheese = input("Do you want  extra cheese ? yes or no. ")

if pizza_choices == "small pizza" :
    bill = 15      
elif pizza_choices == "medium pizza" :
    bill = 20
elif pizza_choices == "large pizza" :
    bill = 25

if add_pepperoni == "yes" :
    if pizza_choices == "small pizza" :
        bill = bill + 2
    else :
        bill = bill + 3
 
if extra_cheese == "yes" :
    bill = bill + 1

print(f"your final bill is:{bill}.")


print(input("\npress enter to exit... "))
