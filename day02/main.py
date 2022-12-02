SCORES = {"A": 1, "B": 2, "C": 3}
WIN = {"A": "B", "B": "C", "C": "A"}
LOSE = {"A": "C", "B": "A", "C": "B"}


def basic(data):
    score = 0
    for game in data:
        if game[0] == game[1]:
            score += 3
        elif WIN[game[0]] == game[1]:
            score += 6
        score += SCORES[game[1]]
    return score


def advanced(data):
    moves = []
    for game in data:
        if game[1] == "A":
            # need to lose
            move = LOSE[game[0]]
        elif game[1] == "B":
            # need to draw
            move = game[0]
        elif game[1] == "C":
            # need to win
            move = WIN[game[0]]
        moves.append([game[0], move])
    return basic(moves)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
        lines = lines.replace("X", "A").replace("Y", "B").replace("Z", "C")
    games = [[x for x in game.split()] for game in lines.split("\n")]

    part1 = basic(games)
    print("First part:", part1)

    part2 = advanced(games)
    print("Second part:", part2)
