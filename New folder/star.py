def print_nested_triangle(n):
    
    print(f"\n--- Nested Loop Triangle Pattern (Height: {n}) ---")
    
    for i in range(n):

        for j in range(i + 1):
            
            # Print '*' on the same line
            print("*", end="") 
        
        # Move to the next line after a row is complete
        print() 
        
    print("-----------------------------------------------------")



n_input_str = input("Enter the height of the triangle : ")

try:
    n = int(n_input_str)
except ValueError:
    # If the user enters text, this is a simple fallback
    n = -1 

if n > 0:
    # If the input is valid (a positive number), call the function
    print_nested_triangle(n)
else:
    # If the input is invalid (zero, negative, or not a number), show an error
    print("\n Invalid input. Please enter a positive whole number (like 1, 2, 3, etc.).")