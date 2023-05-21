from user_interface import User_Interface
from user_interface import Calculator


ui = User_Interface()
calc = Calculator()
# Ask user to choose an operation 
ui.ask_operation()

# Get user input for operation
operation = ui.input_operation()

# Get user input for two numbers
num_1 = ui.user_input1()
num_2 = ui.user_input2()

# Perform operation based on user input
if operation == 1:
    answer = calc.add()
elif operation == 2:
    answer = calc.subtract()
elif operation == 3:
    answer = calc.multiply()
elif operation == 4:
    answer = calc.divide()
else:
    print("Error! Not a valid input. Try again.")
# Display the result
print(answer)
# Ask if the user wants to perform another calculation
