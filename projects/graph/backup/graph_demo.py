#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph

def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    graph.dft_recursive(0)
    print(graph.bfs('0', '3'))
    print(graph.dfs('0', '3'))


if __name__ == '__main__':
    # TODO - parse argv
    main()
