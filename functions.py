"""
This file contains functions that are helpful with solving programming challenges.
"""
from collections.abc import Generator


def read_input(file_path: str) -> list:
    """Reads input from file and returns a list of strings."""
    return [line.rstrip() for line in open(file_path, "r", encoding="utf-8")]


def read_input_int(file_path: str) -> list[int]:
    """Reads input from file and returns a list of integers."""
    return [int(line.rstrip()) for line in open(file_path, "r", encoding="utf-8")]


def multiply(int_list: list[int]) -> int:
    """Multiplies all digits in a list and returns the result."""
    result = 1
    for digit in int_list:
        result *= digit
    return result


def split_list(list_to_split: list, number_of_elements: int) -> Generator:
    """Splits a list into a list of n-element lists."""
    for i in range(0, len(list_to_split), number_of_elements):
        yield list_to_split[i:i + number_of_elements]


def join_list_int(int_list: list[int]) -> int:
    """Joins a list of integers and returns an integer."""
    return int("".join(map(str, int_list)))


def decode_number_from_string(number: str) -> int:
    """Decodes a number from string to integer."""
    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    return number_mapping.get(number, number)