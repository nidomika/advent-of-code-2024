from aocd import data
from itertools import product


lines: list[str] = data.split('\n')

lines: dict[int, list[int]] = {
    int(k): list(map(int, v.split()))
    for k, v in (line.split(": ") for line in lines)
}


def solve(p: dict[int, list[int]], part2: bool = False) -> int:
    total_calibration_score: int = 0

    for key, value in p.items():
        ops: list[str] = ['+', '*', '||'] if part2 else ['+', '*']
        op_combs: list[tuple] = list(product(ops, repeat=len(value) - 1))
        for op_comb in op_combs:
            total: int = value[0]
            for i, op in enumerate(op_comb):
                if op == '+':
                    total += value[i + 1]
                elif op == '*':
                    total *= value[i + 1]
                else:
                    total = int(str(total) + str(value[i + 1]))
            if total == key:
                total_calibration_score += key
                break

    return total_calibration_score


print(solve(lines))
print(solve(lines, True))
