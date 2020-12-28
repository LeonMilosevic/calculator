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
        adds a number to the current state of calculator 'result' attribute
    

    substract(number_to_substract):
        substracts a number from the current state of calculator 'result' attribute


    multiply(multiplier):
        multiplies the current state of calculator 'result' attribute with multiplier


    devide(divisor):
        devides the current state of calculator 'result' attribute with divisor


    sqrt():
        square roots the current state of calculator 'result' attribute


    reset_result():
        sets the current state of calculator 'result' attribute to 0
    """
    def __init__(self, result: float = 0):
        """
        Constructs a default state 'result' attribute if nothing is passed when creating the Calculator class.
        
        Args:
            result: (float, optional)
                State of the class, defaults to 0.
        """
        self.__result = result
    
    @property
    def result(self) -> float:
        """
        Getter for the current state 'result' attribute. Allows user to see their current state of calculator 'result'.

        Returns
        -------
        result: float
            current state of class    
        """
        return self.__result

    # methods
    def add(self, number_to_add: float) -> float:
        """
        Adds the 'number_to_add' to the current state of calculator 'result'. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        number_to_add : int, float

        Returns
        -------
        updated state of calculator 'result' attribute
        """
        self.__result += number_to_add
        return self.__result

    def substract(self, number_to_substract: float) -> float:
        """
        Substracts the current state of calculator 'result' from 'number_to_substract'. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        number_to_substract : int, float

        Returns
        -------
        updated state of calculator 'result' attribute
        """
        self.__result -= number_to_substract
        return self.__result

    def multiply(self, multiplier: float) -> float:
        """
        Multiplies the current state of calculator 'result' with 'multiplier'. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        multiplier : int, float

        Returns
        -------
        updated state of calculator 'result' attribute
        """
        self.__result *= multiplier
        return self.__result

    def devide(self, divisor: float) -> float:
        """
        Devides the current state of calculator 'result' with 'divisor'. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        divisor : int, float

        Returns
        -------
        updated state of calculator 'result' attribute
        """
        self.__result /= divisor
        return self.__result
    
    def sqrt(self) -> float:
        """
        Square roots the current state of calculator 'result' attribute. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        None

        Returns
        -------
        Square rooted state 'result'
        """
        self.__result = self.__result**0.5
        return self.__result
    
    def reset_result(self) -> float:
        """
        Resets the current state of calculator 'result'. Returnes the current state of calculator 'result' attribute.

        Parameters
        ----------
        None

        Returns
        -------
        updated state 'result'
        """
        self.__result = 0
        return self.__result