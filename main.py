# Python = PyScript
from pyscript import display

# Simple Coffee Shop Receipt Generator

# Menu with prices
menu = {
    "Plain Chicken": 120,
    "BBQ Chicken": 169,
    "Spicy Chicken": 169,
    "Honey Chicken": 220,
    "Caramel Chicken": 220
}

# User picks items cause why not 
order = ["Plain Chicken", "BBQ Chicken"]

# Calculate subtotal of chickens
subtotal = sum(menu[item] for item in order)

# VAT (12%)
vat = subtotal * 0.12

# Total
total = subtotal + vat

# Print receipt
print("==== Receipt ====")
print(f"Subtotal: ₱{subtotal:.2f}")
print(f"Tax: ₱{vat:.2f}")
print(f"Total: ₱{total:.2f}")
