import heapq

def find_way(graph):
    queue = []
    start = None
    end = None

    for node in graph.nodes:
        node.cost = float("inf")
        node.visited = False
        node.hidden  = True
        node.prev = None

        if node.value == 0:
            if not start:
                start = node
            else:
                end = node

    start.cost = 0
    queue.append(start)

    while(len(queue)):
        current_node = heapq.heappop(queue)

        if current_node.visited:
            continue

        current_node.visited = True

        if current_node == end:     # found way
            break

        for neighbour in current_node.neighbours:
            if not neighbour.visited:
                if neighbour.cost > current_node.cost + neighbour.value:
                    neighbour.cost = current_node.cost + neighbour.value
                    neighbour.prev = current_node
                    heapq.heappush(queue, neighbour)
    else:   # if len(queue)==0 and not found way
        print("Not found a way.")
        return graph

    node = end
    draw_way = False
    while not draw_way:
        if node == start:
            draw_way = True
        node.hidden = False
        node = node.prev
    return graph