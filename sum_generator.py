import re
from typing import Callable

def generator_numbers(text: str):
    # creating generator, that iterates all real numbers in the text 
    # using regular expression for pattern to indicate nums' 
    pattern = r'\b\d+(\.\d+)?\b'
    # using yeild to create generator
    for match in re.finditer(pattern, text):
        yield match.group()

def sum_profit(text: str, func: Callable):
    # calculating the sum of real numbers from the text using func
    # defining the usage of func for tet
    operation = func(text)
    # comprehension for calculation
    return sum(float(val) for val in operation)

text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")