def add_entry(d):
    d["new_key"] = "new_value"

def reassign_dict(d):
    d = {"reassigned_key": "reassigned_value"}

key = input("Enter dictionary key: ")
value = input("Enter dictionary value: ")
data = {key: value}

print(f"\nDictionary before add_entry: {data}")
add_entry(data)
print(f"Dictionary after add_entry:  {data}")

print(f"\nDictionary before reassign_dict: {data}")
reassign_dict(data)
print(f"Dictionary after reassign_dict:  {data}")
