'''
Description:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(lst: str) -> str:
    new_list = [int(char) for char in lst.split(" ")]
    new_list.sort()
    return f'{new_list[-1]} {new_list[0]}'

assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -50000") == "9 -50000"

# def high_and_low(numbers_str: str) -> str:
#     numbers = [int(num) for num in numbers_str.split()]
#     min_number = numbers[0]
#     max_number = numbers[0]
#     for number in numbers:
#         if number < min_number:
#             min_number = number
#         elif number > max_number:
#             max_number = number
#     else:
#         return f'{max_number} {min_number}'
#
# assert high_and_low("1 2 3 4 5") == "5 1"
# assert high_and_low("1 2 -3 4 5") == "5 -3"
# assert high_and_low("1 9 3 4 -50000") == "9 -50000"