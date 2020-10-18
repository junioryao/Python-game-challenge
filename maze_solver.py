'''
Python Week: Three-Day Challenge
@Annanya Chitra Kannan,
Sanjeet Maisnam,
Kouadio Junior Innocent Yao

Contributions:

    the maze_solver.py code: Sanjeet
    pygame_Launcher.py and other PyGame related materials: Annanya and Junior
    A* algorithm: Annanya

====================================================================================

We create a connected graph whose nodes are only the cells possible to move safely by the pacman. In such, the
complexity of graph operations is reduced tremendously. Having said that, the actual co-ordinates of the path
can be retrieved from the co-ordinates of the nodes.

We apply the Djikstra algorithm to generate the shortest path between two nodes of the graph. We first create a
list of tuples (Key, Door) and sort the list accordingly to set the priority of keys, i.e. the order of keys to
retrieve. We first apply Djikstra from the start point to the first key. We then update the start point to the
first key and apply the algorithm again to go the second key position. In this manner, we keep applying the
algorithm iteratively until we reach the destination.

The python file "pink_cell_class.py" generates the ghost line of sight. It is imported as a module here.
====================================================================================

'''

import networkx as nx
import numpy as np
import os

import pink_cell_class as pcc

from collections import deque
from math import inf as inf
from string import ascii_lowercase

# Just checking the execution time of the code
import timeit

start = timeit.default_timer()


def Djikstra(graph, start, end):
    path = deque()

    #initialize distances of all nodes setting to inf
    distances = {nodes: float(inf) for nodes in graph.nodes}

    # the dictionary with unvisited vertices as keys
    previous_nodes = {nodes: None for nodes in graph.nodes}

    #set the distance of start point to 0
    distances[start] = 0
    unvisited_nodes = [i for i in graph.nodes]

    while unvisited_nodes:
        # 3. Choose the unvisited node with the smallest distance. Make it the current node
        current_node = min(unvisited_nodes, key=lambda vertex: distances[vertex])

        # 6. Break the loop if the smallest distance among the unvisited nodes is infinity.
        if distances[current_node] == inf:
            break

        # 4. Search unvisited neighbors for the current node and calculate their distances through the current node.
        for neighbour in graph.neighbors(current_node):
            alternative_route = distances[current_node] + 1  # +1 for the cost

            # Compare the newly calculated distance to the assigned and get the smaller one.
            if alternative_route < distances[neighbour]:
                distances[neighbour] = alternative_route
                previous_nodes[neighbour] = current_node

        # 5. Mark the current node as visited and remove it from the unvisited set.
        unvisited_nodes.remove(current_node)

    current_node = end
    while previous_nodes[current_node] is not None:
        path.appendleft(current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.appendleft(current_node)

    return path


class Mazesolver:
    def __init__(self, file):
        self.file = file

        with open(self.file, 'r') as f:
            self.nodeslist = np.array([[num for num in line.strip(' \n').split(' ')] for line in f])

        print(self.nodeslist, self.nodeslist.shape)

        self.nodestuples = []

        self.keys = {alphabets: None for rows in self.nodeslist for alphabets in rows if alphabets in ascii_lowercase}

        for k, _ in self.keys.items():
            for i, j in np.argwhere(self.nodeslist == k):
                self.keys[k] = tuple((i, j))

        print("Check-points", self.keys)

        self.checks = self.keys.copy()  # make a copy to perform extra operations while retaining the original keys

        self.checks.__delitem__('s')
        self.checks.__delitem__('e')

        self.checkpoints = [(list(sorted(self.checks))[i], list(sorted(self.checks))[i + 1]) for i in
                            range(0, len(self.checks.keys()), 2)]

        self.checkpoints.insert(0, ('s', 's'))
        self.checkpoints.append(('e', 'e'))

        if ('c', 'd') in self.checkpoints:
            switch = self.checkpoints.index(('c', 'd'))
            self.checkpoints[switch] = self.checkpoints[switch][::-1]

        #keys_for_doors = [keys[0] for keys in self.checkpoints]

        milestones = [keys[0] for keys in self.keys]

        #generate the nodes of the graph to be created
        self.nodestuples = np.array(
            [tuple((i, j)) for i in range(len(self.nodeslist)) for j in range(len(self.nodeslist[i])) if
             self.nodeslist[i][j] in ({'0'}.union(milestones))], dtype='i,i')


        ''' GHOST LIST: create a dict {Ghost range: co-ordinate}'''
        self.ghostdict = {numbers: None for rows in self.nodeslist for numbers in rows if numbers not in ascii_lowercase
                          and numbers not in ['0', '1']}

        for ghost, _ in self.ghostdict.items():
            for i, j in np.argwhere(self.nodeslist == ghost):
                self.ghostdict[ghost] = tuple((i, j))

        print("Ghosts: ", self.ghostdict)

        if self.ghostdict != {} and ('d', 'c') in self.checkpoints:
            swap = self.checkpoints.index(('d', 'c'))
            for i in range(swap, len(self.checkpoints) - 2):
                self.checkpoints[i], self.checkpoints[i + 1] = self.checkpoints[i + 1], self.checkpoints[i]

        #print("{Key: Door}:", self.checkpoints)

        '''--------------------------------------------------'''

        # get the ghost line of sight
        self.d = pcc.get_pink_cell(self.ghostdict, self.nodeslist)

        #print("Pink cells: ", len(self.d), self.d)

        c = []
        for (i, j) in self.nodestuples:
            if (i, j) in self.d:
                c.append(False)
            else:
                c.append(True)

        #remove the nodes corresponding to the pink cells
        self.nodestuples = self.nodestuples[c]
        #print("Nodes after removal: \n", self.nodestuples.shape, self.nodestuples)

        '''-------------------------------------'''

    def Path_tracer(self):

        ''' create a graph with the updated nodes'''
        self.G = nx.DiGraph()
        for (p, q) in self.nodestuples:
            for (i, j) in self.nodestuples:
                l, m = i, j  # next node

                # conditions to add edges
                if (m == q or l == p) and (abs(m - q) == 1 or abs(l - p) == 1):
                    self.G.add_edge((p, q), (l, m))

                else:
                    pass

        '''-----------------------'''
        result = []

        for i in range(len(self.checkpoints) - 1):
            '''Initialize the starting, checkpoints (keys) and destination indexes on the graph'''
            start = self.keys[self.checkpoints[i][0]]
            end = self.keys[self.checkpoints[i + 1][0]]

            result.append(Djikstra(self.G, start, end))


        Path = [j for i in result for j in i]

        return Path


def main():
    file1 = os.path.basename("Maze1.txt")
    file2 = os.path.basename("Maze2.txt")
    file3 = os.path.basename("Maze3.txt")
    file4 = os.path.basename("Maze4.txt")

    # object of the class Mazesolver
    G1 = Mazesolver(file4) #replace this file4 by which file you file

    p1 = G1.Path_tracer()
    print("\n\nPath: ", len(p1), p1)

    # Checking the execution time of the code
    stop = timeit.default_timer()
    print('Code Execution Time: ', stop - start, 's')


if __name__ == "__main__":
    main()
