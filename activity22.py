hight = float(input("Enter the height in cm: "))
weight = float(input("Enter the weight in kg: "))

BMI = weight / ((hight / 100) ** 2)
print("Your BMI is:",BMI)
if BMI <=18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You have a healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are obese (Class 1)")
elif BMI <= 39.9:
    print("You are obese (Class 2)")

    
