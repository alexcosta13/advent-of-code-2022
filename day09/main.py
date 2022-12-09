HEAD_MOVES = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def move(head, tail):
    x, y = head
    i, j = tail
    if abs(x - i) < 2 and abs(y - j) < 2:
        return i, j
    else:
        ver = -1 if x < i else 1 if x > i else 0
        hor = -1 if y < j else 1 if y > j else 0
        i += ver
        j += hor
    return i, j


def basic(data):
    visited = {(0, 0)}
    x, y = 0, 0  # head
    i, j = 0, 0  # tail
    for direction, num in data:
        head = HEAD_MOVES[direction]
        for _ in range(num):
            x += head[0]
            y += head[1]
            if abs(x - i) < 2 and abs(y - j) < 2:
                continue
            else:
                ver = -1 if x < i else 1 if x > i else 0
                hor = -1 if y < j else 1 if y > j else 0
                i += ver
                j += hor
                visited.add((i, j))
    return len(visited)


def advanced(data):
    visited = {(0, 0)}
    positions = [[0, 0] for _ in range(10)]
    for direction, num in data:
        head = HEAD_MOVES[direction]
        for _ in range(num):
            positions[0][0] += head[0]
            positions[0][1] += head[1]
            for i in range(9):
                positions[i + 1] = move(positions[i], positions[i + 1])
            visited.add(tuple(positions[-1]))
    return len(visited)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    moves = [[line.split()[0], int(line.split()[1])] for line in lines.split("\n")]

    part1 = basic(moves)
    print("First part:", part1)

    part2 = advanced(moves)
    print("Second part:", part2)
