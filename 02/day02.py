from aocd import data

input_data = [[int(x) for x in z.split()] for z in data.split("\n")]


def is_valid(p: list[int]) -> bool:
    diffs: list[int] = [p[j - 1] - p[j] for j in range(1, len(p))]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def part1(p: list[list[int]]) -> int:
    return sum(is_valid(r) for r in p)


def part2(p: list[list[int]]) -> int:
    return sum(any(is_valid(r[:i] + r[i + 1:]) for i in range(0, len(r))) for r in p)


print(part1(input_data))
print(part2(input_data))
