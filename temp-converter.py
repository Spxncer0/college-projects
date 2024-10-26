# Started 15/10/23

# Catching user error
while True:
    try:
        temperature = float(input("Enter a temperature: "))
        break
    except ValueError:
        print("Please enter a number")

CELSIUS = temperature * 1.8 + 32
FARENHEIT = (temperature - 32) / 1.8

# Asking the user what metric the degrees is in
while True:
    metric = input("In celsius or farenheit? (c/f): ")
    if metric == "c" or metric == "f":
        break
    else:
        print("Please enter either celsius or farenheit (c/f)")

# Printing the conversion depending on user input
if metric == "c":
    print(f"It is {CELSIUS}° farenheit!")

elif metric == "f":
    print(f"It is {FARENHEIT}° celsius!")
