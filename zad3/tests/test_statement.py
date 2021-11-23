import unittest
from assertpy import assert_that
from src import statement

invoice = {
    "customer": "BigCo",
    "performances": [
          {
              "playID": "hamlet",
                "audience": 55
          },
        {
              "playID": "as-like",
              "audience": 35
          },
        {
              "playID": "othello",
              "audience": 40
          }
    ]
}
plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}

invoice2 = {
    "customer": "OtherCustomer",
    "performances": [
        {
            "playID": "test_play",
                "audience": 1337
        }
    ]
}

plays2 = {
    "test_play": {"name": "test_play", "type": "comedy"}
}


class TestStatement(unittest.TestCase):
    def test_correct_data(self) -> None:
        assert_that(statement(invoice, plays)).is_equal_to(
            "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")

    def test_correct_data_one_play(self) -> None:
        assert_that(statement(invoice2, plays2)).is_equal_to(
            "Statement for OtherCustomer\n test_play: $10,996.00 (1337 seats)\nAmount owed is $10,996.00\nYou earned 1574 credits\n")

    def test_invalid_play_type(self) -> None:
        assert_that(statement).raises(ValueError).when_called_with(
            invoice, {"hamlet": {"name": "Hamlet", "type": "invalid_type"}})

    def test_correct_invoice_empty_plays(self) -> None:
        assert_that(statement).raises(KeyError).when_called_with(invoice, {})

    def test_both_parameters_empty(self) -> None:
        assert_that(statement).raises(KeyError).when_called_with({}, {})
