from typing import Any


def positive_number(argument: int) -> None:
    if argument is None:
        return None
    if type(argument) is not int:
        raise TypeError("Number must be an integer")
    if argument <= 0:
        raise Exception("Number must be a positive integer")


def short_str(argument: str) -> None:
    if argument is None:
        return None
    if len(argument) > 20:
        raise Exception("String too long")


def boolean(argument: bool) -> None:
    if argument is None:
        return None
    if type(argument) is not bool:
        raise TypeError("Argument must be a boolean")
