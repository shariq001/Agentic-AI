# Simple Usage of Callable

from dataclasses import dataclass
from typing import Callable

@dataclass
class Calculator:
    operation : Callable[[int, int], str]

    def __call__(self, a: int, b: int) -> str:
        return self.operation(a, b)


def add_and_stringify(x: int, y: int) -> str:
    return str(x + y)

calc = Calculator(operation=add_and_stringify)

print(calc(5, 13))