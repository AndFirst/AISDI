from dijkstra import find_way
from graph import Graph

if __name__ == "__main__":
    paths = "graph1.txt", "graph2.txt", "graph3.txt"
    for path in paths:
        graph = Graph(path)
        print(graph, end='\n\n')
        print(find_way(graph), end='\n\n')
        print("----------------------------")

