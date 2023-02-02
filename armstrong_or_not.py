def is_armstrong_number(number):
    # Calculate the number of digits in the given number
    num_digits = len(str(number))
    # Initialize the sum
    sum = 0
    # Copy the given number to a temporary variable
    temp = number
    # Iterate over each digit of the number
    while temp > 0:
        # Get the last digit of the number
        digit = temp % 10
        # Add the result of raising the digit to the power of the number of digits to the sum
        sum += digit ** num_digits
        # Remove the last digit from the number
        temp //= 10
    # Return True if the sum is equal to the original number, False otherwise
    return number == sum

# Read a number from the user
number = int(input("Enter a number: "))
# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
