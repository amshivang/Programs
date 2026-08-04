# Take temperature and humidity as input and check if both values are provided
temp_input = input("Enter temperature: ").strip()
humidity_input = input("Enter humidity: ").strip()

if not temp_input and not humidity_input:
    print("Error: Neither temperature nor humidity was provided.")
elif not temp_input:
    print("Error: Temperature is missing.")
elif not humidity_input:
    print("Error: Humidity is missing.")
else:
    print("Success: Both temperature and humidity values were provided.")
    print(f"Temperature: {temp_input}")
    print(f"Humidity   : {humidity_input}")
