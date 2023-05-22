class User_Interface:
    # Ask the user on what operation to use
    def ask_operation(self):
        print("Please choose an operation: \n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division")
        
    def input_operation(self):
        operation = int(input("What operation would you like to use? (1-4): "))
        return operation
    
    # Ask user for two inputs
    def user_input1(self):
        num_1 = float(input("Enter first number: "))
        return num_1

    def user_input2(self):
        num_2 = float(input("Enter second number: "))
        return num_2
    
    # Perform another calculation
    def retry(self):
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if another_calculation.lower() == 'y':
            return True
        # End if user does not want to perform another calculation
        else: 
            print("Thank you for using the simple calculator app!")
            
    # Error Messages        
    # Error message if input for operation is invalid
    def inp_operation_error(self):
        print("Error! Not a valid input for operation. Try again.")
    
    # Error message for zero divison error
    def zero_div_error(self):
        print("Error: Cannot divide by zero!")
    
    # Error message for value error
    def value_error(self):
        print("Error: Invalid input!")

# Calculator operations
class Calculator:
    def add(self, num_1, num_2):
        answer = num_1 + num_2
        return answer
    
    def subtract(self, num_1, num_2):
        answer = num_1 - num_2
        return answer
    
    def multiply(self, num_1, num_2):
        answer = num_1 * num_2
        return answer
    
    def divide(self, num_1, num_2):
        answer = num_1 / num_2
        return answer
    