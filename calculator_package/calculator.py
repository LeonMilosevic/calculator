class Calculator:
    """
    A class that represents a calculator.

    ...

    Attributes
    ----------
    result : int or float
        number that is passed when instantiating a class and a number that will be returned upon applied method
   
    Methods
    -------
    add(number_to_add):
        adds a number to result attribute

    substract(number_to_substract):
        nsubstracts a number from result attribute

    multiply(multiplier):
        multiplies the result attribute with multiplier

    devide(divisor):
        devides the result attribute with divisor

    sqrt():
        square roots the result attribute

    reset_result():
        sets the result attribute to 0
    """
    def __init__(self, result: float = 0):
        """
        Constructs a default result attribute if nothing is passed when creating the Calculator class.
        
        Args:
            result: (float, optional)
                State of the class, defaults to 0.
        """
        self.__result = result
    
    @property
    def result(self) -> float:
        """
        Getter for the result attribute. Allows user to see their current result.

        Returns
        -------
        result: float
            current state of class    
        """
        return self.__result

    # methods
    def add(self, number_to_add: float) -> float:
        """
        Adds the 'number_to_add' to 'result'. Returnes the result attribute.

        Parameters
        ----------
        number_to_add : int, float

        Returns
        -------
        updated 'result'
        """
        self.__result += number_to_add
        return self.__result

    def substract(self, number_to_substract: float) -> float:
        """
        Substracts the 'result' from 'number_to_substract'. Returnes the result attribute.

        Parameters
        ----------
        number_to_substract : int, float

        Returns
        -------
        updated 'result'
        """
        self.__result -= number_to_substract
        return self.__result

    def multiply(self, multiplier: float) -> float:
        """
        Multiplies the 'result' with 'multiplier'. Returnes the result attribute.

        Parameters
        ----------
        multiplier : int, float

        Returns
        -------
        updated 'result'
        """
        self.__result *= multiplier
        return self.__result

    def devide(self, divisor: float) -> float:
        """
        Devides the 'result' with 'divisor'. Returnes the result attribute.

        Parameters
        ----------
        divisor : int, float

        Returns
        -------
        updated 'result'
        """
        self.__result /= divisor
        return self.__result
    
    def sqrt(self) -> float:
        """
        Square roots the current 'result'. Returnes the result attribute.

        Parameters
        ----------
        None

        Returns
        -------
        Square rooted 'result'
        """
        self.__result = self.__result**0.5
        return self.__result
    
    def reset_result(self) -> float:
        """
        Resets the 'result'. Returnes the result attribute.

        Parameters
        ----------
        None

        Returns
        -------
        updated 'result'
        """
        self.__result = 0
        return self.__result