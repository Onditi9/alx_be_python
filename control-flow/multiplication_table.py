# multiplication_table.py

# Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Print multiplication table from 1 to 10
for i in range(1, 11): 
    product = i * number
    print(f"{number} x {i} = {product}")