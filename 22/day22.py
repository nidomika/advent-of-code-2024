from collections import Counter
from aocd import data

lines = list(map(int, data.split('\n')))


def generate_secret(secret: int) -> int:
    secret = (secret * 64 ^ secret) % 16777216
    secret = (secret // 32 ^ secret) % 16777216
    secret = (secret * 2048 ^ secret) % 16777216

    return secret


def part1(p: list[int]) -> int:
    secret_numbers: list[int] = []

    for i, buyer in enumerate(p):
        for _ in range(2000):
            prices[i].append(buyer % 10)
            buyer = generate_secret(buyer)
        secret_numbers.append(buyer)

    return sum(secret_numbers)


def part2() -> int:
    changes: list[list[int]] = []
    for i in range(len(prices)):
        changes.append([])
        for j in range(1, len(prices[i])):
            changes[i].append(prices[i][j] - prices[i][j - 1])

    chunks = Counter()
    for change in changes:
        chunks.update({tuple(change[j:j + 4]) for j in range(len(change) - 3)})
    frequent_chunks: list[tuple[int, int, int, int]] = [k for k, v in chunks.items() if v > 350]

    bananas: list[int] = []
    for chunk in frequent_chunks:
        paid = 0
        for price, diff in zip(prices, changes):
            for i in range(len(diff)):
                if tuple(diff[i:i+4]) == chunk:
                    paid += price[i + 4]
                    break
        bananas.append(paid)

    return max(bananas)

prices = [[] for _ in range(len(lines))]

print(part1(lines))
print(part2())
