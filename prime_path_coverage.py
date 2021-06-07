import itertools

class Graph:
    def __init__(self) -> None:
        # parameters
        self.nodes = None
        self.init_nodes = None
        self.finish_nodes = None
        self.edges = None
        self.init_graph()
        print('Initialized the graph')

    # initializing a graph using console
    def init_graph(self):
        print('Please enter the nodes, separate them with space.')
        print('E.g. 1 2 3 4 for nodes: {1, 2, 3, 4}')
        self.nodes = [int(i) for i in input('> ').split()]
        print('Please specify the initial nodes using the same format used earlier')
        self.init_nodes = [int(i) for i in input('> ').split()]
        print('Please specify the finish nodes using the same format used earlier')
        self.finish_nodes = [int(i) for i in input('> ').split()]
        print('Please specify the edges for each node, use empty line if there is no edge\
            starting from a given node')
        print('E.g. 1: 2 3 6 means we have nodes: {(1, 2), (1, 3), (1, 6)} from node 1')
        self.edges = dict()
        for node in self.nodes:
            self.edges[node] = [int(n) for n in input('{}: '.format(node)).split()]


# building all the simple paths in a graph and then returning it
def find_simple_paths(graph):
    visited = dict()
    for node in graph.nodes:
        visited[node] = False
    simple_paths = []
    for (start, end) in list(itertools.product(graph.nodes, graph.nodes)):
        current_path = []
        DFS(start, end, visited, current_path, simple_paths, graph)
    for node in graph.nodes:
        simple_paths.append([node])
    simple_paths = sorted(simple_paths, key=lambda n: len(n), reverse=True)
    print_paths(simple_paths)
    return simple_paths

# algorithm for finding a simple path starting from node start and ending in node end
def DFS(start, end, visited, current_path, simple_paths, graph):
    if visited[start] == True and end != start:
        return
    visited[start] = True
    current_path.append(start)
    if start == end and len(current_path) > 1:
        simple_paths.append(current_path.copy())
        visited[start] = False
        del(current_path[-1])
        return
    for next in graph.edges[start]:
        DFS(next, end, visited, current_path, simple_paths, graph)
    del(current_path[-1])
    visited[start] = False


# printing a list of paths
def print_paths(paths, label='Paths:'):
    print(label)
    for i in range(len(paths)):
        print('{}: {}'.format(i+1, paths[i]))


# finding prime paths
def find_prime_paths(graph):
    simple_paths = find_simple_paths(graph)
    prime_paths = []
    for f in simple_paths:
        if not any([g for g in prime_paths if (path_in(f, g)) and f != g]):
            prime_paths.append(f)
    print_paths(prime_paths, label='Prime Paths:')


# check whether path f is a sub-sequence in path g
def path_in(f, g):
    return any(map(lambda x: g[x:x + len(f)] == f, range(len(g) - len(f) + 1)))



def main():
    graph = Graph()
    graph.nodes= [1, 2, 3, 4, 5]
    graph.init_nodes= [1]
    graph.finish_nodes= [5]
    graph.edges= {1:[2, 3], 2:[4], 3:[4], 4:[2, 5], 5:[]}
    find_prime_paths(graph)

if __name__ == "__main__":
    main()