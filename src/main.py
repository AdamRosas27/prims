from graph import Graph
# class Main:


class Main:

    def main(self):
        g = Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 2, 15)
        g.add_edge(2, 3, 20)
        g.get_edge_weight(0, 1)
        g.get_all_edges_and_weights()


# if __name__ == '__main__':
#     main = Main()

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()
