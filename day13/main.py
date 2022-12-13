import functools

from pairs import pairs, example
from packets import packets, example


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if right < left:
            return -1
        return 0
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])

    for i in range(len(left)):
        if i == len(right):
            return -1
        aux = compare(left[i], right[i])
        if aux != 0:
            return aux

    if len(left) == len(right):
        return 0
    return 1


def basic(pair_list):
    total = 0
    for i, pair in enumerate(pair_list):
        if compare(*pair) == 1:
            total += i + 1
    return total


def advanced(packet_list):
    packet1 = [[2]]
    packet2 = [[6]]
    packet_list.append(packet1)
    packet_list.append(packet2)

    sorted_packets = sorted(
        packet_list, key=functools.cmp_to_key(compare), reverse=True
    )
    return (sorted_packets.index(packet1) + 1) * (sorted_packets.index(packet2) + 1)


if __name__ == "__main__":
    with open("pairs.py") as f:
        lines = f.read().strip()

    part1 = basic(pairs)
    print("First part:", part1)

    part2 = advanced(packets)
    print("Second part:", part2)
