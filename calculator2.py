from calculator_operations import Calculator

# Child Class
class Calculator2(Calculator):
    def add(self, num_1, num_2):
        answer = num_1 + num_2
        return ("The sum is " + str(answer))
    
    def subtract(self, num_1, num_2):
        answer = num_1 - num_2
        return ("The difference is " + str(answer))
    
    def multiply(self, num_1, num_2):
        answer = num_1 * num_2
        return ("The product is " + str(answer))
    
    def divide(self, num_1, num_2):
        answer = num_1 / num_2
        return ("The quotient is " + str(answer))