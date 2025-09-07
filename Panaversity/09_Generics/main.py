# Means writing code that works with any data type.

# You define a type variable that can be replaced with any type.

# Helps make functions or classes reusable and type-safe.

from typing import TypeVar


nums = [1, 2, 3, 4]
strings = ["a", "b", "c", "d"]

# Type variable for generic typing
T = TypeVar("T")

def generic_first_element(items: list[T]) -> T:
    return items[0]

num_resutlt = generic_first_element(nums)
string_result = generic_first_element(strings)

print(num_resutlt)
print(string_result)

# Ex 2: Dict 2 diff inputs

K = TypeVar('K') # Keys
V = TypeVar('V') # Values

def get_item(container: dict[K, V], key: K) -> V:
    return container[key]

d = {"a": 1, "b": 2}

value = get_item(d, "b")
print(value)
