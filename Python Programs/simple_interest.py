# Calculate simple interest using the formula SI = (P * R * T) / 100
try:
    principal = float(input("Enter the Principal amount (P): "))
    rate = float(input("Enter the annual Rate of interest (R in %): "))
    time = float(input("Enter the Time period (T in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Principal, Rate, and Time must be non-negative values.")
    else:
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest
        print(f"\nPrincipal Amount  : {principal:.2f}")
        print(f"Rate of Interest  : {rate:.2f}%")
        print(f"Time Period       : {time:.2f} years")
        print(f"Simple Interest   : {simple_interest:.2f}")
        print(f"Total Amount (P+SI): {total_amount:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
