def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def ideal_weight_range(height_m):
    min_wt = round(18.5 * (height_m ** 2), 2)
    max_wt = round(24.9 * (height_m ** 2), 2)
    return min_wt, max_wt

def main():
    print("=== BMI Calculator ===")
    print("1. Calculate BMI & Category")
    print("2. Find Ideal Weight Range")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        w = float(input("Enter Weight (kg): "))
        h = float(input("Enter Height (m): "))
        bmi = calculate_bmi(w, h)
        print(f"BMI = {bmi} ({get_bmi_category(bmi)})")
    elif choice == "2":
        h = float(input("Enter Height (m): "))
        low, high = ideal_weight_range(h)
        print(f"Ideal Weight Range = {low} kg to {high} kg")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
