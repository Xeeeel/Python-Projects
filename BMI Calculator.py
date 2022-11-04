# BMI Calculator
# Developed by Xel

# Notes before proceeding to the BMI Calculator
print("Notes: Make sure that your height is in meter and your weight is in kilograms.")

# The client's information
Name = input("Enter your name: ")
Age = input("Enter your age:" )

# The height and weight of the Client
Height = float(input("Kindly enter your height: "))
Weight = int(input("Kindly enter your weight: "))

# The formula of BMI kg/m^2
formula = Weight / (Height**2)

# The result of the client's BMI
print("Here is your BMI result: " + str(formula))

# The BMI Categories
if formula < 18.5:
    print("Hi " + Name + ", You're in the underweight range.")
elif formula <= 24.9:
    print("Hi " + Name + ", You're in the healthy weight range.")
elif formula <= 29.9:
    print("Hi " + Name + ", You're in the overweight range.")
elif formula >= 30:
    print("Hi " + Name + ", You're in the obese range.")

# Blank Space
print("")

# Thank you for using our BMI Calculator.
print("Thank you for using our BMI Calculator!")