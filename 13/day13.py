from aocd import data
from sympy import Matrix, solve_linear_system
from sympy.abc import a, b


lines = [[[int(z[2:]) for z in y.split(": ")[1].split(', ')]
          for y in x.split('\n')]
         for x in data.split("\n\n")]


def solve_part(part: int, p: list[list[list[int]]]) -> int:
    presses = 0

    for equation in p:
        system = Matrix(equation).T
        solved = solve_linear_system(system, a, b)

        if solved[a].is_integer and solved[b].is_integer:
            if part != 1 or (solved[a] <= 100 and solved[b] <= 100):
                presses += 3 * solved[a] + solved[b]

    return presses


print(solve_part(1, lines))
print(solve_part(2, [line[:2] + [[line[2][0] + 10000000000000,
      line[2][1] + 10000000000000]] for line in lines]))
