# 7. BMI = m/h2, m based kg, h based meter

def calculateBMI(m, h):
    BMI = m / (h * 2)
    if (BMI <= 15):
        print("Extremely underweight and dangerous")
    elif (15 < BMI <= 16):
        print("Extremely underweight")
    elif (16 < BMI <= 18.5):
        print("Underweight")
    elif (18.5 < BMI <= 25):
        print("Normal")
    elif (25 < BMI <= 30):
        print("Overweight")
    elif (30 < BMI <= 35):
        print("Obese")
    elif (35 < BMI <= 40):
        print("Extremely Obese")
    elif (40 < BMI):
        print("Extremely Obese and dangerous")


while (True):
    try:
        height = float(input("Please enter your height based on meter: "))
        mass = float(input("Please enter your weight based on kilogram: "))

        if (height <= 0 or mass <= 0):
            print("The mass and weight cannot be zero or negative, please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continued.")

calculateBMI(mass, height)





