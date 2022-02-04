# 1. A regular Python function

def double(n: int) -> int:
    return n * 2

num = double(21)
print(num)


# 2. Collection types

def average(nums: list[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average([1, 2, 3, 4]))


def get_total_marks(scorecard: dict[str, int]) -> int:
    marks_list = scorecard.values()
    return sum(marks_list)

scores = {'english': 84, 'maths': 92, 'history': 75}
print(get_total_marks(scores))


# Extras: variable annotation syntax

magic_number: int = 42  # This doesn't actually define magic_number


# 3. Unions

lucky_numbers = (5, 7)

deck_of_cards = [10, 2, 7, 3, 1]
chosen_card: int | str = 'not found in deck'

for card in deck_of_cards:
    if card in lucky_numbers:
        chosen_card = card

print("Chosen card:", chosen_card)


def buy(stuff: str | list[str]) -> None:
    if isinstance(stuff, list):
        for item in stuff:
            print("Buying", item)

    else:
        print("Buying", stuff)

buy('milk')
buy(['spam', 'eggs', 'brownies'])


# 4. Any type

from typing import Any

def print_user_info(user: dict[str, Any]) -> None:
    name = user['name']
    age = user['age']
    print("User's name is:", name)
    print("User's age is:", age)


user = {
    'name': 'Tushar',
    'age': 21,
    'height': 176.8,
}
print_user_info(user)


def untyped_function(data: Any) -> Any:
    # reveal_type(data)
    for item in data.split(','):
        # reveal_type(item)
        print(item)


# 5. Classes


class Stack:
    def __init__(self) -> None:
        self._values: list[int] = []

    def __repr__(self) -> str:
        return f'Stack{self._values!r}'

    def push(self, value: int) -> None:
        self._values.append(value)

    def pop(self) -> int:
        if len(self._values) == 0:
            raise RuntimeError('Underflow!')

        return self._values.pop()

stack = Stack()
print(stack)

stack.push(2)
stack.push(10)
print(stack)

popped_value = stack.pop()
print("Popped value:", popped_value)
print(stack)


# Extras: Literals

from typing import Literal

def http_request(method: Literal['GET', 'POST', 'PUT'], url: str) -> None:
    ...

http_request('GET', 'https://api.example.com')
http_request('PSOT', 'https://api.example.com')  # Typo!
