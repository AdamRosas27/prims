# class Graph:
class Graph:

    # def __init__(self):
    # pass
    def __init__(self):
        self.adj_list = {}

# def add_vertex(self, vertex):
# pass

    # Implement error handling, if user inputs strings as vertex, throw error
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

# def add_edge(self, vertex1, vertex2, weight):
# pass
    # Implement error handling, if user inputs strings as vertex1, vertex2, and weight throw error
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list:
            self.adj_list[vertex1].append((vertex2, weight))
        else:
            self.adj_list[vertex1] = [(vertex2, weight)]

# get_edge_weight(self, vertex1, vertex2):
# pass

    # Implement error handling, if user inputs strings as vertex1, vertex2, throw error
    def get_edge_weight(self, vertex1, vertex2):
        # Add edge case if vertex1/vertex2 dont exist
        if vertex1 in self.adj_list:
            for neighbor, weight in self.adj_list[vertex1]:
                if neighbor == vertex2:
                    print(weight)
        return None

# prims():
# pass

# get_all_edges_and_total_weight(self):
# pass

    def get_all_edges_and_weights(self):
        for vertex in range(len(self.adj_list)):
            edges = self.adj_list.get(vertex, [])
            edge_str = ", ".join([str(edge[0]) if edge[0]
                                 is not None else "None" for edge in edges])
            print(f"Vertex: {vertex} --> Edges: {edge_str}")
