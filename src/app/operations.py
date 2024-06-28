class Calculator:
    """
    A calculator class.
    """


    def __init__(self) -> None:
        """
        Initialize the calculator
        """
        
        self.result: int | float = 0


    def add(self, num: int | float) -> None:
        """
        Add a number to the current result.

        Args:
            num (int or float): The number to add.
        """

        self.result += num


    def subtract(self,num: int | float) -> None:
        """
        Subtract a number to the current result.

        Args:
            num (int or float): The number to subtract.
        """
        self.result -= num


    def multiply(self, num: int | float) -> None:
        """
        Multiply a number to the current result.

        Args:
            num (int or float): The number to multiply.
        """

        self.result *= num


    def divide(self, num: int | float) -> int | float:
        """
        Divide a number to the current result.

        Args:
            num (int or float): The number to divide.
        """

        try:
            self.result /= num
        except ZeroDivisionError:
            print("Você não pode dividir por 0.")


    def get_result(self,) -> int | float:
        """
        Get the current result.

        Returns:
            int or float: The current result.
        """
        return self.result