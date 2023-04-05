class Node:

    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.cost = float("inf")
        self.visited = False
        self.hidden = False
        self.prev = None

    def __str__(self):
        if self.hidden:
            return " "
        else:
            return str(self.value)

    def __lt__(self, other):
        return self.cost < other.cost

    def add_neighbour(self, node):
        self.neighbours.append(node)


class Graph:
    def __init__(self, path):
        self.read_from_file(path)

    def __str__(self):
        text = ""
        for i, node in enumerate(self.nodes):
            text += str(node)

            if i % self.width == self.width - 1:
                text += '\n'
        return text[:-1]

    def read_from_file(self, path):
        self.nodes = []

        with open(path) as file:
            for line in file:
                for value in list(line.rstrip()):
                    self.nodes.append((Node(int(value))))
            self.width = len(line)

        for i, node in enumerate(self.nodes):
            if i % self.width != 0:
                node.add_neighbour(self.nodes[i-1])
            if i % self.width != self.width-1:
                node.add_neighbour(self.nodes[i+1])
            if i < len(self.nodes) - self.width:
                node.add_neighbour(self.nodes[i + self.width])
            if i >= self.width:
                node.add_neighbour(self.nodes[i-self.width])
