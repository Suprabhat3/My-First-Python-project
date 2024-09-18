# my first python project for oder food in cafe



menu = {
    "pasta": 10,
    "burger": 8,
    "pizza": 10, 
    "coffee": 5
}
order_total = 0
print("Here is the menu:\n", menu)

# First order
order = input("What do you want to order: ").lower()

if order in menu:
    order_total += menu[order]
    print(f"Your order is {order} and your total is: {order_total}")
else:
    print(f"Your order {order} is not available yet.")

# Reorder loop
while True:
    reorder = input("\nDo you want anything else (yes/no): ").lower()
    
    if reorder == "no":
        break  # Exit the loop if no more orders

    order2 = input("What else would you like to order: ").lower()
    
    if order2 in menu:
        order_total += menu[order2]
        print(f"Your orders are {order} and {order2}, and your total is: {order_total}")
    else:
        print(f"Your order {order2} is not available yet.")

print(f"Final total: {order_total}")
