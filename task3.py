import heapq
import networkx as nx
import matplotlib.pyplot as plt


def init_network():
    G = nx.Graph()

    G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                     "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    G.add_edge("A", "B", weight=10)
    G.add_edge("A", "C", weight=8)
    G.add_edge("A", "D", weight=5)
    G.add_edge("D", "E", weight=7)
    G.add_edge("D", "F", weight=6)
    G.add_edge("C", "Z", weight=3)
    G.add_edge("Z", "O", weight=9)
    G.add_edge("O", "F", weight=1)
    G.add_edge("O", "V", weight=1)
    G.add_edge("O", "P", weight=6)
    G.add_edge("V", "P", weight=7)
    G.add_edge("B", "I", weight=8)
    G.add_edge("I", "H", weight=2)
    G.add_edge("I", "S", weight=3)
    G.add_edge("S", "T", weight=6)
    G.add_edge("S", "J", weight=5)
    G.add_edge("H", "J", weight=5)
    G.add_edge("J", "K", weight=5)
    G.add_edge("E", "G", weight=5)
    G.add_edge("H", "G", weight=4)
    G.add_edge("F", "L", weight=6)
    G.add_edge("L", "Q", weight=7)
    G.add_edge("L", "G", weight=10)
    G.add_edge("Q", "M", weight=5)
    G.add_edge("Q", "X", weight=3)
    G.add_edge("M", "R", weight=4)
    G.add_edge("M", "K", weight=2)
    G.add_edge("G", "K", weight=7)
    G.add_edge("N", "K", weight=8)
    G.add_edge("N", "R", weight=4)
    G.add_edge("N", "U", weight=6)
    G.add_edge("R", "Y", weight=10)
    G.add_edge("P", "W", weight=3)

    return G


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())
    # print(unvisited)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        # print(current_vertex)
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in graph[current_vertex].items():
            w = weight['weight']
            # print(neighbor, " ", w)
            distance = distances[current_vertex] + w
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


def dijkstra_heap(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist
        for neighbor, weight in graph[node].items():
            w = weight['weight']
            heapq.heappush(heap, (dist + w, neighbor))

    return distances


def nx_dijkstra(graph, start):
    return nx.single_source_dijkstra_path_length(graph, source=start)


if __name__ == "__main__":
    G = init_network()

    print('\n Standart Dijkstra \n')
    print(dijkstra(G, 'A'))
    print('\n Dijkstra with heapq \n')
    print(dijkstra_heap(G, 'A'))
    print('\n Dijkstra from networkx library \n')
    print(nx_dijkstra(G, 'A'))
