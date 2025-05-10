# BMI Calculator 

# This program calculates the Body Mass Index (BMI) based on user input for weight and height.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2) # formula for BMI

bmi = weight / (height **2)

if bmi < 18.5:
    print("you are underweight.")

elif 18.5 <= bmi < 25 :
    print("you have a normal weght.")
elif 25 <= bmi < 30:
    
    print("you have normal weight.")
else :
    print("you are obese.")

print (f"yor bmi is {bmi:.2f}")