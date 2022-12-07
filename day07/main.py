class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.size = None
        self.children = []
        self.parent = parent

    def get_size(self):
        if self.size:
            return self.size
        total = 0
        for child in self.children:
            total += child.get_size()
        self.size = total
        return total

    def get_all_children_dir(self):
        aux = [child for child in self.children if isinstance(child, Directory)]
        for child in self.children:
            if isinstance(child, Directory):
                aux.extend(child.get_all_children_dir())
        return aux

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child


def parse(cmd_list):
    parent = Directory("/")
    current_dir = parent
    for cmd in cmd_list[1:]:
        parts = cmd.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.get_child(parts[2])
        else:
            if parts[0] == "dir":
                current_dir.children.append(Directory(parts[1], current_dir))
            else:
                current_dir.children.append(File(parts[1], int(parts[0])))

    parent.get_size()
    return parent


def basic(parent):
    return sum([c.size for c in parent.get_all_children_dir() if c.size < 100_000])


def advanced(parent):
    free_space = 70000000 - parent.get_size()
    return min(
        [
            c.size
            for c in parent.get_all_children_dir()
            if c.size > 30000000 - free_space
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()
    cmds = [cmd for cmd in lines.split("\n")]

    parent = parse(cmds)

    part1 = basic(parent)
    print("First part:", part1)

    part2 = advanced(parent)
    print("Second part:", part2)
