
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height * height)
bmi_round = round(bmi)

if bmi < 18.5:
  print(f"Your BMI is {bmi_round} ,you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi_round} ,you have normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi_round} ,you are slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi_round} ,you are obese")
elif bmi > 35:
  print(f"Your BMI is {bmi_round} ,you are clinically obese")
