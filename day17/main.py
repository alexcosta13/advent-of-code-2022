ROCKS = [
    {(2, 0), (3, 0), (4, 0), (5, 0)},
    {(2, 1), (3, 0), (3, 1), (4, 1), (3, 2)},
    {(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)},
    {(2, 0), (2, 1), (2, 2), (2, 3)},
    {(2, 0), (2, 1), (3, 0), (3, 1)},
]

EXAMPLE = False


def move(rock, direction):
    x, y = direction
    return {(i + x, j + y) for (i, j) in rock}


def basic(moves, number_of_rocks=2022):
    cave = set()
    j = 0
    for i in range(number_of_rocks):
        initial_y = max(cave, key=lambda x: x[1])[1] + 4 if len(cave) > 0 else 3
        falling_rock = ROCKS[i % 5]
        falling_rock = move(falling_rock, (0, initial_y))
        while True:
            direction = (1, 0) if moves[j % len(moves)] == ">" else (-1, 0)
            new_position = move(falling_rock, direction)
            if any(p in cave or p[0] < 0 or p[0] > 6 for p in new_position):
                pass
            else:
                falling_rock = new_position
            j += 1

            new_position = move(falling_rock, (0, -1))
            if any(p in cave or p[1] < 0 for p in new_position):
                cave |= falling_rock
                break
            else:
                falling_rock = new_position

    return max(cave, key=lambda x: x[1])[1] + 1


def inspect(moves, number_of_rocks=10_000):
    cave = set()
    j = 0
    final_positions = []
    for i in range(number_of_rocks):
        initial_y = max(cave, key=lambda x: x[1])[1] + 4 if len(cave) > 0 else 3
        falling_rock = ROCKS[i % 5]
        falling_rock = move(falling_rock, (0, initial_y))
        while True:
            direction = (1, 0) if moves[j % len(moves)] == ">" else (-1, 0)
            new_position = move(falling_rock, direction)
            if any(p in cave or p[0] < 0 or p[0] > 6 for p in new_position):
                pass
            else:
                falling_rock = new_position
            j += 1

            new_position = move(falling_rock, (0, -1))
            if any(p in cave or p[1] < 0 for p in new_position):
                cave |= falling_rock
                final_positions.append(min(falling_rock, key=lambda x: x[0])[0])
                break
            else:
                falling_rock = new_position

        if i % 5 == 4:
            print(tuple(final_positions))
            final_positions = []


if __name__ == "__main__":
    with open("example.txt" if EXAMPLE else "input.txt") as f:
        moves = f.read().strip()

    part1 = basic(moves)
    print("First part:", part1)

    # START and END manually found by running (line number of the start and end of the repeated sequence)
    # implement(moves)
    START, END = (110, 449) if not EXAMPLE else (3, 10)
    part2 = basic(
        moves, 5 * START + ((1000000000000 - 5 * START) % (5 * (END - START)))
    ) + ((1000000000000 - 5 * START) // (5 * (END - START))) * (
        basic(moves, 5 * END) - basic(moves, 5 * START)
    )
    print("Second part:", part2)
