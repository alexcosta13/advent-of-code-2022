import numpy as np


def is_visible(grid, x, y):
    if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
        return True
    if max(grid[x, :y]) < grid[x, y]:
        return True
    if max(grid[x, y + 1:]) < grid[x, y]:
        return True
    if max(grid[:x, y]) < grid[x, y]:
        return True
    if max(grid[x + 1:, y]) < grid[x, y]:
        return True
    return False


def scenic_score(grid, x, y):
    up, down, right, left = 0, 0, 0, 0
    if x == 0:
        return 0
    if y == 0:
        return 0
    if x == len(grid):
        return 0
    if y == len(grid):
        return 0
    for i in range(x - 1, -1, -1):
        up += 1
        if grid[i][y] >= grid[x][y]:
            break
    for i in range(x + 1, len(grid)):
        down += 1
        if grid[i][y] >= grid[x][y]:
            break
    for j in range(y - 1, -1, -1):
        left += 1
        if grid[x][j] >= grid[x][y]:
            break
    for j in range(y + 1, len(grid)):
        right += 1
        if grid[x][j] >= grid[x][y]:
            break
    return up * down * right * left


def basic(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if is_visible(data, i, j):
                total += 1
    return total


def advanced(data):
    max_scenic_score = 0
    for i in range(len(data)):
        for j in range(len(data)):
            current_scenic_score = scenic_score(data, i, j)
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score
    return max_scenic_score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    plantation = [[int(tree) for tree in line] for line in lines.split("\n")]
    plantation = np.array(plantation)

    part1 = basic(plantation)
    print("First part:", part1)

    part2 = advanced(plantation)
    print("Second part:", part2)
