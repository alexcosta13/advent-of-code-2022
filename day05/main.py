from queue import LifoQueue
from re import findall, compile


def create_queues(example=False):
    if example:
        queue1 = LifoQueue()
        queue1.put("Z")
        queue1.put("N")
        queue2 = LifoQueue()
        queue2.put("M")
        queue2.put("C")
        queue2.put("D")
        queue3 = LifoQueue()
        queue3.put("P")

        return {1: queue1, 2: queue2, 3: queue3}

    else:
        queue1 = LifoQueue()
        for item in "TPZCSLQN":
            queue1.put(item)
        queue2 = LifoQueue()
        for item in "LPTVHCG":
            queue2.put(item)
        queue3 = LifoQueue()
        for item in "DCZF":
            queue3.put(item)
        queue4 = LifoQueue()
        for item in "GWTDLMVC":
            queue4.put(item)
        queue5 = LifoQueue()
        for item in "PWC":
            queue5.put(item)
        queue6 = LifoQueue()
        for item in "PFJDCTSZ":
            queue6.put(item)
        queue7 = LifoQueue()
        for item in "VWGBD":
            queue7.put(item)
        queue8 = LifoQueue()
        for item in "NJSQHW":
            queue8.put(item)
        queue9 = LifoQueue()
        for item in "RCQFSLV":
            queue9.put(item)
        return {
            1: queue1,
            2: queue2,
            3: queue3,
            4: queue4,
            5: queue5,
            6: queue6,
            7: queue7,
            8: queue8,
            9: queue9,
        }


def result(q):
    res = ""
    for i in range(len(q)):
        res += q[i + 1].get()
    return res


def basic(moves, queues):
    for move in moves:
        for _ in range(move[0]):
            item = queues[move[1]].get(False)
            queues[move[2]].put(item)
    return result(queues)


def advanced(moves, queues):
    for move in moves:
        aux = LifoQueue()
        for _ in range(move[0]):
            aux.put(queues[move[1]].get(False))
        for _ in range(move[0]):
            queues[move[2]].put(aux.get(False))
    return result(queues)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    instruction = [
        list(map(int, findall(compile(r"(\d+)"), line)))
        for line in lines.split("\n\n")[1].split("\n")
    ]

    position = create_queues()

    part1 = basic(instruction, position)
    print("First part:", part1)

    position = create_queues()

    part2 = advanced(instruction, position)
    print("Second part:", part2)
