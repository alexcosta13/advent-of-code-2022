def basic(data, decryption_key=1, mixing_rounds=1):
    data = [i * decryption_key for i in data]
    original = [i for i in range(len(data))]
    for _ in range(mixing_rounds):
        for i in range(len(original)):
            idx = original.index(i)
            item = data.pop(idx)
            original_item = original.pop(idx)
            new_idx = (idx + item) % len(original)
            if new_idx == 0:
                data.append(item)
                original.append(original_item)
            else:
                data.insert(new_idx, item)
                original.insert(new_idx, original_item)
    zero_idx = data.index(0)
    return sum([data[(i * 1000 + zero_idx) % len(data)] for i in range(1, 4)])


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    sequence = [int(line) for line in lines.split("\n")]

    part1 = basic(sequence)
    print("First part:", part1)

    sequence = [int(line) for line in lines.split("\n")]
    part2 = basic(sequence, decryption_key=811589153, mixing_rounds=10)
    print("Second part:", part2)
