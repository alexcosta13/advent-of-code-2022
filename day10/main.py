def get_history(data):
    current_value = 1
    history = [0]
    for instruction in data:
        history.append(current_value)
        if instruction.split()[0] == "addx":
            history.append(current_value)
            current_value += int(instruction.split()[1])
    return history


def basic(data):
    history = get_history(data)
    signal_strength = sum(
        [v * i for i, v in enumerate(history) if i in [20, 60, 100, 140, 180, 220]]
    )
    return signal_strength


def advanced(data):
    history = get_history(data)[1:]
    picture = []
    for pos, sprite in enumerate(history):
        if abs((pos % 40) - sprite) < 2:
            picture.append("#")
        else:
            picture.append(" ")

    for i, j in enumerate(picture):
        print(j, end="")
        if not (i + 1) % 40:
            print()
    return


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    instructions = [line for line in lines.split("\n")]

    part1 = basic(instructions)
    print("First part:", part1)

    print("Second part:")
    advanced(instructions)
