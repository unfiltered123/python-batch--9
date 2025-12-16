'''mylist = [1,2,3]
print("A list : %s" %mylist)
'''



# 1. Define variables
item_name = "Toaster Oven"
item_price = 79.501
item_quantity = 5

print("-" * 40)

#  %d (Decimal Integer) ---
stock_id = 14
print("Item ID: %03d" % stock_id)

# %s (String) ---
print("Item Name: %-15s | Quantity: %d" % (item_name, item_quantity))

# %f (Floating Point Number) ---
print("Unit Price: $%.3f" % item_price)

# Example: Using width and precision (%10.2f)
total_cost = item_price * item_quantity
print("Total Cost: $%10.2f" % total_cost)

# Combining all three ---
final_summary = "Order: %d units of %s @ $%.2f each." % (
    item_quantity, 
    item_name, 
    item_price
)
print("-" * 40)
print(final_summary)
print("-" * 40)