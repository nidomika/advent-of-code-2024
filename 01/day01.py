from aocd import data
from collections import Counter

input_data = [[int(value) for value in line.split()] for line in data.split("\n")]
input_data = list(zip(*input_data[::-1]))


def part1(lists: list[list[int]]) -> int:
    lists = [sorted(x) for x in lists]
    return sum(abs(n - m) for n, m in zip(*lists))


def part2(lists: list[list[int]]) -> int:
    counter = Counter(lists[1])
    return sum([num * counter.get(num, 0) for num in lists[0]])


print(part1(input_data))
print(part2(input_data))
