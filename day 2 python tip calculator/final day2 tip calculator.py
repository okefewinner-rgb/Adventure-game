print(("hello") +" " +  input("what is your name?"))
print("welcome to the tip calculator!")
total_bill= input("what is the total bill:$")
percent_tip=input("how much tip will you like to give? 10,12,or15? ")
percent_tip_int=int((percent_tip))
total_bill_int=(int(total_bill))
people_involved= input("how many people are to split the bill? ")
people_involved_int=int(people_involved)
amount_tip= total_bill_int * (percent_tip_int/100)
amount_to_be_shared= total_bill_int + (amount_tip)
total_bill_per_person= amount_to_be_shared/(people_involved_int)
print(total_bill_per_person)
print(f"Each person should pay:${total_bill_per_person:.2f}")




input("\nPress Enter to exit...")