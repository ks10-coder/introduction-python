x = float(input("What is x? "))
y = float(input("What is y? "))

#Use f-strings to format the output to 2 decimal places
z = round(x / y, 2)

print(f"{z:.2f}")