from math import prod
from re import findall, compile

EXAMPLE = False


def operation_example(monkey, stress):
    if monkey == 0:
        return stress * 19
    elif monkey == 1:
        return stress + 6
    elif monkey == 2:
        return stress * stress
    elif monkey == 3:
        return stress + 3


def operation(monkey, stress):
    if monkey == 0:
        return stress * 13
    elif monkey == 1:
        return stress * stress
    elif monkey == 2:
        return stress + 6
    elif monkey == 3:
        return stress + 2
    elif monkey == 4:
        return stress + 3
    elif monkey == 5:
        return stress + 4
    elif monkey == 6:
        return stress + 8
    elif monkey == 7:
        return stress * 7


def parse(data):
    m = dict()
    for i, monkey in enumerate(data):
        m[i] = [
            list(map(int, findall(compile(r"(\d+)"), monkey.split("\n")[1]))),
            list(map(int, findall(compile(r"(\d+)"), monkey.split("\n")[3])))[0],
            list(map(int, findall(compile(r"(\d+)"), monkey.split("\n")[4])))[0],
            list(map(int, findall(compile(r"(\d+)"), monkey.split("\n")[5])))[0],
        ]
    return m


def inspect_items(data, i, advance=False):
    monkey = data[i]
    for item in monkey[0]:
        item = operation_example(i, item) if EXAMPLE else operation(i, item)
        item = (
            int(item / 3)
            if not advance
            else item % prod([monkey[1] for monkey in data.values()])
        )
        if not item % monkey[1]:
            data[monkey[2]][0].append(item)
        else:
            data[monkey[3]][0].append(item)
    data[i][0] = []
    return data


def play(data, rounds=20, advance=False):
    counter = dict()
    for k in range(rounds):
        for i in range(len(data)):
            counter[i] = (
                counter[i] + len(data[i][0]) if i in counter else len(data[i][0])
            )
            data = inspect_items(data, i, advance)
    return prod(sorted(counter.values())[-2:])


if __name__ == "__main__":
    with open("example.txt" if EXAMPLE else "input.txt") as f:
        lines = f.read().strip()
    lines = [line for line in lines.split("\n\n")]

    monkeys = parse(lines)
    part1 = play(monkeys)
    print("First part:", part1)

    monkeys = parse(lines)
    part2 = play(monkeys, rounds=10_000, advance=True)
    print("Second part:", part2)
