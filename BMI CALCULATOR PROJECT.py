### BMI CALCULATOR PROJECT ###

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = weight / pow(height, 2)
print(f"Your BMI is {round(BMI, 2)} kg/m^2")

if BMI < 16:
    print("You have severe thinness.")
elif 16 <= BMI < 17:
    print("You have moderate thinness.")
elif 17 <= BMI < 18.5:
    print("You have mild thinness.")
elif 18.5 <= BMI < 25:
    print("You have healthy weight.")
elif 25 <= BMI < 30:
    print("You are overweight.")
elif 30 <= BMI < 35:
    print("You are classified as Obese Class I.")
elif 35 <= BMI < 40:
    print("You are classified as Obese Class II.")
else:
    print("You are classified as Obese Class III.")