import os.path

from graph import Node, Graph
from dijkstra import find_way

def test_create_node():
    node = Node(0)
    assert node.value == 0
    assert len(node.neighbours) == 0
    assert node.value == float("inf")
    assert node.visited is False
    assert node.hidden is False
    assert node.prev is None

def test_node_str():
    node = Node(0)
    assert node.__str__() == "0"

    node.hidden = True
    assert node.__str__() == " "

def test_add_neighbour():
    node = Node(0)
    neighbour = Node(1)
    node.add_neighbour(neighbour)
    assert node.neighbours[0] == neighbour
    assert len(node.neighbours == 1)

def test_load_graph_from_file():
    # create test file
    file = open("foo.txt", "w")
    file.write("011\n111\n110")
    file.close()

    graph = Graph("foo.txt")

    # remove test file
    if os.path.isfile("foo.txt"):
        os.remove("foo.txt")
    assert graph.width == 3
    assert graph.__str__() == "011\n111\n110"

def test_find_way():
    # create test file
    file = open("foo.txt", "w")
    file.write("011\n111\n110")
    file.close()

    graph = Graph("foo.txt")

    # remove test file
    if os.path.isfile("foo.txt"):
        os.remove("foo.txt")

    graph = find_way(graph)
    assert graph.__str__() == "011\n  1\n  0"
