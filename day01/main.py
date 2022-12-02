if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    calories = [
        sum([int(food) for food in elf.split("\n")]) for elf in lines.split("\n\n")
    ]

    part1 = max(calories)
    print("First part:", part1)

    part2 = sum((sorted(calories)[-3:]))
    print("Second part:", part2)
