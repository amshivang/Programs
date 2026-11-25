# Calculate in-hand salary after HRA (10%), DA (5%), PF (3%), and tax deductions
try:
    salary = float(input("Enter annual gross salary (in INR): "))

    if salary < 0:
        print("Salary cannot be negative.")
    else:
        lakhs = salary / 100000.0

        # Determine tax rate based on salary brackets
        if lakhs < 5:
            tax_percent = 0
        elif lakhs <= 10:
            tax_percent = 10
        elif lakhs <= 20:
            tax_percent = 20
        else:
            tax_percent = 30

        hra = 0.10 * salary
        da = 0.05 * salary
        pf = 0.03 * salary
        tax = (tax_percent / 100.0) * salary

        total_deductions = hra + da + pf + tax
        in_hand_salary = salary - total_deductions

        print("\n--- Salary Breakdown ---")
        print(f"Gross Salary       : Rs. {salary:,.2f}")
        print(f"HRA Deduction (10%): Rs. {hra:,.2f}")
        print(f"DA Deduction (5%)  : Rs. {da:,.2f}")
        print(f"PF Deduction (3%)  : Rs. {pf:,.2f}")
        print(f"Tax Deduction ({tax_percent}%): Rs. {tax:,.2f}")
        print("------------------------")
        print(f"In-Hand Salary     : Rs. {in_hand_salary:,.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
