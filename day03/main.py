def value(item):
    v = ord(item)
    if 97 <= v <= 122:
        return v - 96
    else:
        return v - 65 + 27


def basic(data):
    priorities = 0
    for bag in data:
        item = (set(bag[:int(len(bag) / 2)]) & set(bag[int(len(bag) / 2):])).pop()
        priorities += value(item)
    return priorities


def advanced(data):
    result = 0
    for i in range(int(len(data) / 3)):
        elf1 = set(data[i * 3])
        elf2 = set(data[i * 3 + 1])
        elf3 = set(data[i * 3 + 2])
        badge = (elf1 & elf2 & elf3).pop()
        result += value(badge)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    bags = [items for items in lines.split("\n")]

    part1 = basic(bags)
    print("First part:", part1)

    part2 = advanced(bags)
    print("Second part:", part2)
