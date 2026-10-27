print("hello "+"" + input("what is your name? ")+ " " + "This is a body mass index(BMI) calculator! ")

print("BMI= weight(kg)/(height**2(m^2))")

weight=input("what is your weight in kg: ")
weight_in_float= float(weight)

height=input("what is your height in m: ")
height_in_float= float(height)

bmi= round(weight_in_float/ (height_in_float**2),0)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi},you have a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi},you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi},you are obese.")
else:
    print(f"your bmi is {bmi},you are clinically obese.")



input("\npress Enter to exit...")