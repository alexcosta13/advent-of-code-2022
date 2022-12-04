def is_contained(a, b):
    if a[0] <= b[0] and a[1] >= b[1]:
        return True
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    return False


def overlaps(a, b):
    if a[1] < b[0] or a[0] > b[1]:
        return False
    return True


def basic(data):
    return sum([is_contained(*i) for i in data])


def advanced(data):
    return sum([overlaps(*i) for i in data])


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    sectors = [
        [[int(i) for i in elf.split("-")] for elf in line.split(",")]
        for line in lines.split("\n")
    ]

    part1 = basic(sectors)
    print("First part:", part1)

    part2 = advanced(sectors)
    print("Second part:", part2)
