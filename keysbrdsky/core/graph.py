from collections import deque

import hashlib
import package.vertex as vertex
Vertex = vertex.Vertex

#вот это вынеси в отдельный файл, чтооб он был в модуле core
class BaseEdge(Vertex):

    def __new__(cls,start,end,cost):
        self = super(BaseEdge, cls).__new__(cls, start, end, cost)
        return self
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_cost(self):
        return self.cost

inf = float('inf')
class Graph():
    def __init__(self, edges):

        #if len(edges) != 3:
        #    raise ValueError('Wrong edges data: {}'.format(edges))
        self.edges = [BaseEdge(edge[0], edge[1], edge[2]) for edge in edges]


    @property
    def vertices(self):
        return set(
            sum(
                ([edge.get_start(), edge.get_end()] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        node_pairs = [[n1, n2], [n2, n1]] if both_ends else [[n1, n2]]

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.get_start(), edge.get_end()] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.get_start(), edge.get_end()] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(BaseEdge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(BaseEdge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.get_start()].add((edge.get_end(), edge.get_cost()))

        return neighbours

    def dijkstra(self, source, dest):
        print(self.vertices)
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex, arr_p = deque(), dest, list()
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            print(path)
            #print(distances[current_vertex])
            arr_p.append(distances[current_vertex])
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return (path, arr_p)


def test():
    graph = Graph([
        Vertex("a", "b", 7),  Vertex("a", "c", 9),  Vertex("a", "f", 14), Vertex("b", "c", 10),
        Vertex("b", "d", 15), Vertex("c", "d", 11), Vertex("c", "f", 2),  Vertex("d", "e", 6),
        Vertex("e", "f", 9)])

    return graph.dijkstra('84312883a7fcbf9d9e6d180df58ba912745084e7', 'ac7236c78e55892a3de2cba496963bd3c7656a5f')
