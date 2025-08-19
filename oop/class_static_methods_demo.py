class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the class attribute."""
        print(f"Calculation Type: {cls.calculation_type}")  # lowercase 'type'
        return a * b 
    

if __name__ == "__main__":
    result_sum = Calculator.add(10, 5)
    print(f"The sum is: {result_sum}")

    result_product = Calculator.multiply(10, 5)
    print(f"The product is: {result_product}")
