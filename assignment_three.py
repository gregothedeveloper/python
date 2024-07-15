def math_operations(num1, num2):
    """
    Perform mathematical operations on two numbers.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    tuple: A tuple containing the sum and product of num1 and num2.
    """
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y

    sum_result = add(num1, num2)
    product_result = multiply(num1, num2)

    return sum_result, product_result

def main():
    # Getting user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calling math_operations function
    sum_result, product_result = math_operations(num1, num2)

    # Printing results
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

# Calling the main function to execute the program
main()
