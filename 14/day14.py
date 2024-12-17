from aocd import data

lines = data.split('\n')
lines = [{y.split('=')[0]: tuple(map(int, y.split('=')[1].split(','))) for y in x.split()} for x in lines]

wide = 101
tall = 103


def part1(p: list[dict[str, tuple[int, ...]]]) -> int:
    for robot in p:
        robot['p'] = (robot['p'][0] + 100 * robot['v'][0]) % wide, (robot['p'][1] + 100 * robot['v'][1]) % tall

    conditions = [
        (lambda x: x < wide // 2, lambda y: y < tall // 2),
        (lambda x: x > wide // 2, lambda y: y < tall // 2),
        (lambda x: x > wide // 2, lambda y: y > tall // 2),
        (lambda x: x < wide // 2, lambda y: y > tall // 2),
    ]

    result = 1
    for x_cond, y_cond in conditions:
        result *= sum(1 for point in p if x_cond(point['p'][0]) and y_cond(point['p'][1]))

    return result


def part2(p: list[dict[str, tuple[int, ...]]]) -> int:
    seconds = 0

    while len(set(list(map(lambda x: x['p'], p)))) < len(p):
        seconds += 1
        p = [{'p': ((robot['p'][0] + robot['v'][0]) % wide, (robot['p'][1] + robot['v'][1]) % tall), 'v': robot['v']}
             for robot in p]

    return seconds


print(part1(lines))
print(part2(lines))
