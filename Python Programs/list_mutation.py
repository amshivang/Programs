def remove_last(lst):
    if lst:
        lst.pop()

items = input("Enter list elements separated by space: ").split()
print(f"List before function call: {items}")
remove_last(items)
print(f"List after function call:  {items}") 
