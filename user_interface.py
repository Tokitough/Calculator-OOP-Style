class User_Interface:
    def ask_operation(self):
        print("Please choose an operation: \n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division")
        
    def input_operation(self):
        operation = int(input("What operation would you like to use? (1-4): "))
        return operation
       
    def user_input1(self):
        num_1 = float(input("Enter first number: "))
        return num_1

    def user_input2(self):
        num_2 = float(input("Enter second number: "))
        return num_2