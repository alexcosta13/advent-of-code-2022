def value(item):
    v = ord(item)
    if 97 <= v <= 122:
        return v - 96
    else:
        return v - 65 + 27


def basic(data):
    priorities = 0
    for bag in data:
        comp1 = bag[:int(len(bag) / 2)]
        comp2 = bag[int(len(bag) / 2):]
        repeated = set()
        for item in comp1:
            if item in comp2:
                repeated.add(item)
        for item in repeated:
            priorities += value(item)
    return priorities


def advanced(data):
    result = 0
    for i in range(int(len(data) / 3)):
        elf1 = data[i * 3]
        elf2 = data[i * 3 + 1]
        elf3 = data[i * 3 + 2]
        badge = set()
        for item in elf1:
            if item in elf2 and item in elf3:
                badge.add(item)
        for item in badge:
            result += value(item)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    bags = [items for items in lines.split("\n")]

    part1 = basic(bags)
    print("First part:", part1)

    part2 = advanced(bags)
    print("Second part:", part2)
