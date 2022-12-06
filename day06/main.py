def find_header(data, header_length=4):
    for i in range(len(data)):
        if len(list(set(data[i:i + header_length]))) == header_length:
            return i + header_length
    raise NotImplemented


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = find_header(lines)
    print("First part:", part1)

    part2 = find_header(lines, header_length=14)
    print("Second part:", part2)
