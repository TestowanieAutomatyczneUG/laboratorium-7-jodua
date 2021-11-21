class PasswordValidator:
    def __init__(self) -> None:
        self.upperCount = 0
        self.numberCount = 0
        self.otherCount = 0

    def ValidPassword(self, password: str) -> bool:
        """
        Test ValidPassword (requirements: 1 uppercase, 1 digit, 1 special, length>8)
        >>> pv.ValidPassword("zaq1@WSX")
        True
        >>> pv.ValidPassword("IASBDUddHIASBD1213241123123!@##1")
        True
        >>> pv.ValidPassword("")
        False
        >>> pv.ValidPassword("zaq12WSX")
        False
        >>> pv.ValidPassword("zaq!@WSX")
        False
        >>> pv.ValidPassword("zaq1@wsx")
        False
        >>> pv.ValidPassword("123123123123")
        False
        >>> pv.ValidPassword(123123123)
        Traceback (most recent call last):
        ...
        TypeError: Invalid password type
        """
        if type(password) is not str:
            raise TypeError("Invalid password type")
        else:
            self.upperCount = 0
            self.numberCount = 0
            self.otherCount = 0

            for c in password:
                if c.isupper():
                    self.upperCount += 1
                elif c.isdigit():
                    self.numberCount += 1
                elif not c.isalpha():
                    self.otherCount += 1

            if len(password) < 8:
                return False

            if self.upperCount < 1:
                return False
            if self.numberCount < 1:
                return False
            if self.otherCount < 1:
                return False
            return True


if __name__ == "__main__": #pragma: no cover
    import doctest
    doctest.testmod(extraglobs={'pv': PasswordValidator()})
