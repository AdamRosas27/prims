# class Graph:
class Graph:

    # def __init__(self):
    # pass
    def __init__(self):
        self.adj_list = {}

# def add_vertex(self, vertex):
# pass

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

# def add_edge(self, vertex1, vertex2, weight):
# pass

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list:
            self.adj_list[vertex1].append((vertex2, weight))
        else:
            self.adj_list[vertex1] = [(vertex2, weight)]

# get_edge_weight(self, vertex1, vertex2):
# pass

    def get_edge_weight(self, vertex1, vertex2):
        # Add edge case if vertex1/vertex2 dont exist
        if vertex1 in self.adj_list:
            for neighbor, weight in self.adj_list[vertex1]:
                if neighbor == vertex2:
                    return weight
        return None

# prims():
# pass

# get_all_edges_and_total_weight(self):
# pass
