def odd_or_even(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Get user input
try:
    number = int(input("Enter a number: "))
    result = odd_or_even(number)
    print(result)
except ValueError:
    print("Please enter a valid integer.")


'''
The try and except block ensures that the program handles invalid inputs gracefully 
by catching ValueError exceptions if the input is not a valid integer
'''



# Function to input a number, if the number is odd then return a string "ODD" and if the number is even then return a string "EVEN"