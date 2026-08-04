# Menu-driven conversion program
def cm_to_inches():
    try:
        cm = float(input("Enter length in centimeters (cm): "))
        inches = cm / 2.54
        print(f"{cm} cm = {inches:.4f} inches")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def km_to_miles():
    try:
        km = float(input("Enter distance in kilometers (km): "))
        miles = km * 0.62137119
        print(f"{km} km = {miles:.4f} miles")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def usd_to_inr():
    try:
        usd = float(input("Enter amount in USD ($): "))
        # Using a fixed exchange rate (e.g. 83.50 INR per USD)
        rate = 83.50
        inr = usd * rate
        print(f"${usd} USD = Rs. {inr:.2f} INR (Exchange rate: 1 USD = {rate} INR)")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\n=== CONVERSION MENU ===")
        print("a. Convert cm to inches")
        print("b. Convert km to miles")
        print("c. Convert USD to INR")
        print("d. Exit")
        choice = input("Enter your choice (a/b/c/d): ").strip().lower()

        if choice == 'a':
            cm_to_inches()
        elif choice == 'b':
            km_to_miles()
        elif choice == 'c':
            usd_to_inr()
        elif choice == 'd':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a, b, c, or d.")

if __name__ == "__main__":
    main()
