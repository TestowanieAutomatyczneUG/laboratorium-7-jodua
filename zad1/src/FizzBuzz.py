class FizzBuzz:
    def game(self, number: int) -> str:
        """FizzBuzz game that checks divisibility by 3 and 5
        >>> g.game(3)
        'Fizz'
        >>> g.game(999999999999999999999)
        'Fizz'
        >>> g.game(123123123)
        'Fizz'
        >>> g.game(-3)
        'Fizz'
        >>> g.game(5)
        'Buzz'
        >>> g.game(55555555)
        'Buzz'
        >>> g.game(55)
        'Buzz'
        >>> g.game(-5)
        'Buzz'
        >>> g.game(15)
        'FizzBuzz'
        >>> g.game(7)
        '7'
        >>> g.game(23)
        '23'
        >>> g.game(113)
        '113'
        >>> g.game(2137)
        '2137'
        >>> g.game(1337)
        '1337'
        >>> g.game(0)
        'FizzBuzz'
        >>> g.game(0b1111)
        'FizzBuzz'
        >>> g.game(0xA)
        'Buzz'
        >>> g.game("invalid")
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game(3.14)
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game([1,2,3,4])
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game((8,9))
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game({"A":1})
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game(False)
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        >>> g.game(None)
        Traceback (most recent call last):
        ...
        TypeError: Invalid type (should be int)
        """
        output = ""
        if type(number) != int:
            raise TypeError("Invalid type (should be int)")
        else:
            if number % 3 == 0:
                output += "Fizz"
            if number % 5 == 0:
                output += "Buzz"
            if output != "":
                return output
            else:
                return str(number)


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'g': FizzBuzz()})
