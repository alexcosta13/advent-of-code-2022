def snafu_to_decimal(snafu):
    decimal = 0
    for i, n in enumerate(snafu[::-1]):
        value = int(n) if n in "012" else -1 if n == "-" else -2
        decimal += value * 5**i
    return decimal


def decimal_to_snafu(decimal):
    snafu = ""
    while decimal > 0:
        aux = decimal % 5
        value = aux if aux < 3 else -2 if aux == 3 else -1
        decimal -= value
        decimal //= 5
        snafu += str(aux) if aux < 3 else "=" if aux == 3 else "-"
    return snafu[::-1]


def basic(data):
    return decimal_to_snafu(sum([snafu_to_decimal(number) for number in data]))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    numbers = lines.split("\n")

    part1 = basic(numbers)
    print("First part:", part1)
