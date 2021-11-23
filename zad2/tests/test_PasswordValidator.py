import unittest
from assertpy import assert_that
from src import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = PasswordValidator()

    def test_valid_password(self) -> None:
        assert_that(self.temp.ValidPassword("zaq1@WSX")).is_true()

    def test_valid_password_2(self) -> None:
        assert_that(self.temp.ValidPassword("UG2@2!ug")).is_true()

    def test_long_password_without_numbers(self) -> None:
        assert_that(self.temp.ValidPassword(
            "AIOSJDHNASIODBASOUIDHBASDOUIHASBDASUIOHBD!@(#&*lijabdsklhjb")).is_false()

    def test_long_valid_password(self) -> None:
        assert_that(self.temp.ValidPassword(
            "AIOSJDHNASIODBASOUIDH123123123BDASUIOHBD!@(#&*lijabdsklhjb")).is_true()

    def test_password_too_short(self) -> None:
        assert_that(self.temp.ValidPassword("zaq1@WS")).is_false()

    def test_password_no_uppercase_letters(self) -> None:
        assert_that(self.temp.ValidPassword("zaq1@wsx")).is_false()

    def test_password_no_digits(self) -> None:
        assert_that(self.temp.ValidPassword("zaqWSX@!")).is_false()

    def test_password_no_lowercase_letters(self) -> None:
        assert_that(self.temp.ValidPassword(
            "OAUHSBDASIHDBHUJIDASBD!@#!@#!)@)&#!@7123")).is_true()

    def test_password_no_special_letters(self) -> None:
        assert_that(self.temp.ValidPassword("zaq12wsxXXXs")).is_false()

    def test_password_only_special_characters(self) -> None:
        assert_that(self.temp.ValidPassword("!@#$%^&*(){}\":?>")).is_false()

    def test_password_only_digits(self) -> None:
        assert_that(self.temp.ValidPassword(
            "12312385673405620578640576254056")).is_false()

    def test_password_only_uppercase(self) -> None:
        assert_that(self.temp.ValidPassword(
            "XSDCFVGBHNJKJNHBUVYCTFRXCYVBPKLMLJSANDASKJLDNASLKJN")).is_false()

    def test_password_empty_string(self) -> None:
        assert_that(self.temp.ValidPassword("")).is_false()

    def test_password_int(self) -> None:
        assert_that(self.temp.ValidPassword).raises(
            TypeError).when_called_with(123123)

    def test_password_list(self) -> None:
        assert_that(self.temp.ValidPassword).raises(
            TypeError).when_called_with(["a", "b", "c"])

    def test_password_obj(self) -> None:
        assert_that(self.temp.ValidPassword).raises(
            TypeError).when_called_with({"test": 1})

    def test_password_none(self) -> None:
        assert_that(self.temp.ValidPassword).raises(
            TypeError).when_called_with(None)

    def test_password_bool(self) -> None:
        assert_that(self.temp.ValidPassword).raises(
            TypeError).when_called_with(False)

    def tearDown(self) -> None:
        self.temp = None
