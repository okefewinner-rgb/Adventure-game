





age= input("what is your current age? ")
age_as_int = int(age)

years_remaining = 90-age_as_int


daysremaining = years_remaining*365
weeksremaining =years_remaining*52
monthsremaining =years_remaining*12

message= f"you have {daysremaining}days,{weeksremaining}weeks,and{monthsremaining}months left."
print(message)

input("\nPress Enter to exit...")
