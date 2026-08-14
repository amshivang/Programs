def generate_bill(*args, **kwargs):
    prices = list(args)
    items = list(kwargs.items())
    
    total_bill = 0.0
    total_quantity = 0
    
    max_items = max(len(prices), len(items))
    for i in range(max_items):
        if i < len(items):
            item_name, qty = items[i]
            qty = int(qty)
            price = prices[i] if i < len(prices) else 0.0
        else:
            item_name = f'Unnamed Item {i - len(items) + 1}'
            qty = 1
            price = prices[i]
            
        item_total = price * qty
        total_bill += item_total
        total_quantity += qty
        print(f'{item_name} (Qty: {qty}): Rs. {item_total:.2f}')
        
    avg_price = sum(prices) / len(prices) if prices else 0.0
    print(f'Total Quantity: {total_quantity}')
    print(f'Average Price: {avg_price:.2f}')
    print(f'Subtotal: {total_bill:.2f}')
    
    discount = 0.0
    if total_bill > 5000:
        discount = 0.10 * total_bill
        print(f'Discount: {discount:.2f}')
        
    print(f'Final Payable Amount: {total_bill - discount:.2f}')

num_items = int(input('Enter number of items: '))
prices = []
quantities = {}
for i in range(1, num_items + 1):
    name = input(f'Enter item {i} name: ').strip()
    price = float(input(f'Enter unit price for {name}: '))
    qty = int(input(f'Enter quantity for {name}: '))
    prices.append(price)
    quantities[name] = qty
    
generate_bill(*prices, **quantities)
