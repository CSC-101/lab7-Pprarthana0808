

from typing import List
from convert import str_to_float


def gather_numbers() -> List[float]:

    numbers = []

    while True:
        user_input = input("Enter a number or type 'done' to end: ").strip()
        if user_input.lower() == "done":
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
        else:
            print(f"'{user_input}' is not a valid number. Please try again.")
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print("Sum of numbers:", sum(numbers))
