from graph import Graph
# class Main:


class Main:

    def main(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(4)
        g.add_vertex(5)
        g.add_vertex(6)
        g.add_vertex(7)
        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 4)
        g.add_edge(1, 6, 5)
        g.add_edge(1, 4, 7)
        g.add_edge(2, 1, 2)
        g.add_edge(2, 4, 6)
        g.add_edge(2, 7, 8)
        g.add_edge(2, 5, 3)
        g.add_edge(3, 1, 4)
        g.add_edge(3, 6, 6)
        g.add_edge(4, 1, 7)
        g.add_edge(4, 2, 6)
        g.add_edge(4, 6, 1)
        g.add_edge(4, 7, 6)
        g.add_edge(5, 2, 3)
        g.add_edge(5, 7, 7)
        g.add_edge(6, 3, 6)
        g.add_edge(6, 1, 5)
        g.add_edge(6, 4, 1)
        g.add_edge(6, 7, 6)
        g.add_edge(7, 6, 6)
        g.add_edge(7, 4, 6)
        g.add_edge(7, 2, 8)
        g.add_edge(7, 5, 7)
        g.get_edge_weight(0, 1)
        mst = g.prims(1)
        print("\nMinimum Spanning Tree (MST):")
        for u, v, weight in mst:
            print(
                f"Edge: {u}-{v}, Weight: {weight}")
        total_mst_weight = 0
        for _, _, weight in mst:
            total_mst_weight += weight
        g.get_all_edges_and_total_weight()
        print(f"Total Minimum Spanning Tree Weight: {total_mst_weight}")


# if __name__ == '__main__':
#     main = Main()

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
