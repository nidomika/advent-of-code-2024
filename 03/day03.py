from aocd import data
import re


def part1(p: str) -> int:
    mul_sum: int = 0

    for match in re.finditer(r"mul\(\d+,\d+\)", p):
        a, b = map(int, match.group()[4:-1].split(","))
        mul_sum += a * b

    return mul_sum


def part2(p: str) -> int:
    mul_sum: int = 0

    p = p.split("do")
    mul_sum += part1(p[0])

    for line in p[1:]:
        if line.startswith("()"):
            mul_sum += part1(line)

    return mul_sum


print(part1(data))
print(part2(data))