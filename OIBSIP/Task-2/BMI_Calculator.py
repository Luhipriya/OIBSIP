def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("===========================")
    print("     BMI CALCULATOR")
    print("===========================\n")

    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        if weight <= 0 or height <= 0:
            print("\nInvalid input. Please enter positive values only.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\nCalculating...\n")
        print(f"Your BMI is: {bmi}")
        print(f"Category: {category}")
        print("\nStay healthy and fit!")
    except ValueError:
        print("\nError: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
