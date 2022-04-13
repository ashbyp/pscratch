import csv
import collections
import pprint


class Graph:

    @classmethod
    def from_csv(cls, filename, directed=True):
        g = cls([], directed)
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                g.add_connection(row[0], row[1])
        return g

    def __init__(self, connections, directed=True):
        self._graph = collections.defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add_connection(node1, node2)

    def add_connection(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def print(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self._graph)

    def find_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    data = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    g1 = Graph(data, True)
    g1.print()
    g2 = Graph(data, False)
    g2.print()
    g3 = Graph.from_csv('data.csv')
    g3.print()

    print(g3.find_path('a', 'd'))
