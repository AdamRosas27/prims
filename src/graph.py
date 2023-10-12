import heapq

# class Graph:


class Graph:

    # def __init__(self):
    def __init__(self):
        self.adj_list = {}

# def add_vertex(self, vertex):
    # Implement error handling, if user inputs int as vertex, throw error
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

# def add_edge(self, vertex1, vertex2, weight):
    # Implement error handling, if user inputs strings as vertex1, vertex2, and weight throw error
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list:
            self.adj_list[vertex1].append((vertex2, weight))
        else:
            self.adj_list[vertex1] = [(vertex2, weight)]

# get_edge_weight(self, vertex1, vertex2):
    # Implement error handling, if user inputs strings as vertex1, vertex2, throw error
    def get_edge_weight(self, vertex1, vertex2):
        # Add edge case if vertex1/vertex2 dont exist
        if vertex1 in self.adj_list:
            for neighbor, weight in self.adj_list[vertex1]:
                if neighbor == vertex2:
                    print(weight)
        return None

# prims():
    def prims(self, starting_vertex):
        visited = set()
        mst_edges = []
        min_heap = []

        def add_edges(vertex):
            visited.add(vertex)
            for neighbor, weight in self.adj_list[vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, vertex, neighbor))

        add_edges(starting_vertex)

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)
            if v not in visited:
                mst_edges.append((u, v, weight))
                add_edges(v)

        return mst_edges


# get_all_edges_and_total_weight(self):

    def all_edges(self):
        print(f"\nVertex --> Corresponding Edge(s)")
        for vertex in range(1, len(self.adj_list) + 1):
            edges = self.adj_list.get(vertex, [])
            edge_str = ", ".join(
                [str(edge[0]) if edge[0] is not None else "None" for edge in edges])
            print(f"Vertex: {vertex} --> Edges: {edge_str}")

    def total_weight_no_mst(self):

    def get_all_edges_and_total_weight(self):
        print(f"\nVertex --> Corresponding Edge(s)")
        for vertex in range(1, len(self.adj_list) + 1):
            edges = self.adj_list.get(vertex, [])
            edge_str = ", ".join(
                [str(edge[0]) if edge[0] is not None else "None" for edge in edges])
            print(f"Vertex: {vertex} --> Edges: {edge_str}")
