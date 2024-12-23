from itertools import combinations
from aocd import data

lines = data.split('\n')

computers = set(item for row in lines for item in row.split("-"))
connections = set()

for line in lines:
    a, b = line.split('-')
    connections.update([(a, b), (b, a)])


def part1() -> int:
    combs = list(combinations(computers, 3))
    count = 0

    for comb in combs:
        if all({(comb[0], comb[1]) in connections,
                (comb[1], comb[2]) in connections,
                (comb[2], comb[0]) in connections}):
            if 't' in ''.join(comb)[::2]:
                count += 1

    return count


def part2() -> str:
    networks = [{x} for x in computers]

    for network in networks:
        for computer1 in computers:
            if all((computer2, computer1) in connections for computer2 in network):
                network.add(computer1)

    return ','.join(sorted(max(networks, key=len)))


print(part1())
print(part2())
