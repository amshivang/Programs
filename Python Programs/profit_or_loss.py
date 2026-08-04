# Calculate profit or loss based on cost price and selling price
try:
    cost_price = float(input("Enter the Cost Price (CP): "))
    selling_price = float(input("Enter the Selling Price (SP): "))

    if selling_price > cost_price:
        profit = selling_price - cost_price
        percentage = (profit / cost_price) * 100
        print(f"Profit of: {profit:.2f} (Percentage: {percentage:.2f}%)")
    elif cost_price > selling_price:
        loss = cost_price - selling_price
        percentage = (loss / cost_price) * 100
        print(f"Loss of: {loss:.2f} (Percentage: {percentage:.2f}%)")
    else:
        print("No Profit, No Loss (Break-even).")
except ValueError:
    print("Invalid input. Please enter valid numeric values for prices.")
except ZeroDivisionError:
    print("Cost price cannot be zero when calculating percentages.")
