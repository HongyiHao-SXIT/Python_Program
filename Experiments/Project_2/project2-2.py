weight = float(input("Please enter your weight (kg): "))
height = float(input("Please enter your height (m): "))

bmi = weight / (height ** 2)

print(f"The value of BMI is: {bmi:.2f}")

if bmi < 18.5:
    level = "Underweight. You are too light. You should increase your nutrition."
elif 18.5 <= bmi < 24:
    level = "Normal. You are in excellent health. Great!"
elif 24 <= bmi < 28:
    level = "Overweight. Regular work and rest and a reasonable diet will make you healthy."
else:
    level = "Obese. Keeping a healthy body is a way to take care of yourself. You should exercise."

print("Your physical condition is: ", level)