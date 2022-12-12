def get_neighbors(origin, grid):
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    i, j = origin
    current = grid[i][j]
    if current == "S":
        current = "a"
    if current == "E":
        current = "z"

    for move in moves:
        x = i + move[0]
        y = j + move[1]
        if (
            0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and ord(grid[x][y]) < ord(current) + 2
        ):
            yield x, y


def dijkstra(start, end, grid, advance=False):
    distance = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "a" and advance:
                distance[(i, j)] = 0
            else:
                distance[(i, j)] = 1_000_000

    distance[start] = 0
    to_visit = distance.copy()

    while len(to_visit) > 0:
        current = min(to_visit, key=to_visit.get)
        if current == end:
            return distance[current]

        del to_visit[current]

        for n in get_neighbors(current, grid):
            if distance[current] + 1 < distance[n]:
                distance[n] = distance[current] + 1
            if n in to_visit:
                to_visit[n] = distance[current] + 1

    return distance


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    grid = [[p for p in line] for line in lines.split("\n")]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = i, j
            if grid[i][j] == "E":
                end = i, j

    part1 = dijkstra(start, end, grid)
    print("First part:", part1)

    part2 = dijkstra(start, end, grid, advance=True)
    print("Second part:", part2)
