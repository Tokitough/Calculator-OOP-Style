from user_interface import UserInterface
from calculator_operations import Calculator
from calculator2 import Calculator2


ui = UserInterface()
calc = Calculator()
calc_2 = Calculator2()

def calculator():
    try:
        # Ask user to choose an operation 
        ui.ask_operation()

        # Get user input for operation
        operation = ui.input_operation()
        
        # Get user input for two numbers
        num_1 = ui.user_input1()
        num_2 = ui.user_input2()
        
        # Perform operation based on user input
        if operation == 1:
            answer = calc_2.add(num_1, num_2)
        elif operation == 2:
            answer = calc_2.subtract(num_1, num_2)
        elif operation == 3:
            answer = calc_2.multiply(num_1, num_2)
        elif operation == 4:
            answer = calc_2.divide(num_1, num_2)   
        else:
            ui.inp_operation_error()
            calculator()          

        # Display the result
        ui.result(answer)
        
        # Ask if the user wants to perform another calculation
        if ui.retry() == True:
            calculator()
    
    # Handle division by zero error    
    except ZeroDivisionError:
            ui.zero_div_error()
            calculator()
    
    # Handle invalid input error
    except ValueError:
            ui.value_error()
            calculator()
        
calculator()