# Define a function that calculates the sum of the input number
def sum(number1, number2):
    return number1 + number2



if __name__ == "__main__":

    input_number1 = float(input("Please enter the first number.："))
    input_number2 = float(input("Please enter the second number："))

    result = sum(input_number1, input_number2)
    print(f"The sum of {input_number1} and {input_number2} is {result}")