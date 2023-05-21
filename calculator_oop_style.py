from user_interface import User_Interface
from user_interface import Calculator


ui = User_Interface()
calc = Calculator()

def calculator():
    try:
        # Ask user to choose an operation 
        ui.ask_operation()

        # Get user input for operation
        operation = ui.input_operation()
        
        # Perform operation based on user input
        if operation == 1:
            answer = calc.add(num_1, num_2)
        elif operation == 2:
            answer = calc.subtract(num_1, num_2)
        elif operation == 3:
            answer = calc.multiply(num_1, num_2)
        elif operation == 4:
            answer = calc.divide(num_1, num_2)   
        else:
            print("Error! Not a valid input for operation. Try again.")
            calculator()
            
        # Get user input for two numbers
        num_1 = ui.user_input1()
        num_2 = ui.user_input2()

        # Display the result
        print(answer)
        # Ask if the user wants to perform another calculation
        ui.retry
        
    except ZeroDivisionError:
            # Handle division by zero error
            print("Error: Cannot divide by zero.")
            calc.calculator()
    except ValueError:
            # Handle invalid input error
            print("=" * 45)
            print("Error: Invalid input.")
            calc.calculator()
        
calculator()