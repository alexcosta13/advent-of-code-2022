def parse(paths):
    cave = set()
    for path in paths:
        lines = path.split(" -> ")
        for i in range(len(lines) - 1):
            a, b = list(map(int, lines[i + 1].split(",")))
            x, y = list(map(int, lines[i].split(",")))
            if x == a:
                for k in range(y, b + 1):
                    cave.add((x, k))
                for k in range(b, y + 1):
                    cave.add((x, k))
            elif y == b:
                for k in range(x, a + 1):
                    cave.add((k, y))
                for k in range(a, x + 1):
                    cave.add((k, y))
            else:
                raise Exception("x != a and y != b")
    return cave


def basic(cave):
    initial = len(cave)
    max_vertical_position = max([position[1] for position in list(cave)])
    while True:
        i, j = 500, 0
        while True:
            if j > max_vertical_position:
                return len(cave) - initial
            elif (i, j + 1) not in cave:
                j += 1
            elif (i - 1, j + 1) not in cave:
                i -= 1
                j += 1
            elif (i + 1, j + 1) not in cave:
                i += 1
                j += 1
            else:
                cave.add((i, j))
                break


def advanced(cave):
    initial = len(cave)
    max_vertical_position = max([position[1] for position in list(cave)]) + 1
    while True:
        i, j = 500, 0
        if (i, j) in cave:
            return len(cave) - initial
        while True:
            if j == max_vertical_position:
                cave.add((i, j))
                break
            elif (i, j + 1) not in cave:
                j += 1
            elif (i - 1, j + 1) not in cave:
                i -= 1
                j += 1
            elif (i + 1, j + 1) not in cave:
                i += 1
                j += 1
            else:
                cave.add((i, j))
                break


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    caves = parse([line for line in lines.split("\n")])

    part1 = basic(caves)
    print("First part:", part1)

    caves = parse([line for line in lines.split("\n")])
    part2 = advanced(caves)
    print("Second part:", part2)
