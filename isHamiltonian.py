'''
Determines if a given graph is hamiltonian.

Parameters:
    graph: a dictionary representing a graph.
    eg. the K4 graph would be represented by {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}.
'''
class IsHamiltonian():
    def Checker(graph):
        unvisited = list(graph.keys())
        visited = []
        i = 0
        v = unvisited.pop()
        initial = v
        visited.append(v)
        while unvisited != 0:
            if len(visited) == len(list(graph.keys())):
                return True
            if i > len(graph[v]) - 1:
                return False
            if graph[v][i] not in visited and graph[v][i] in list(graph.keys()):
                v = graph[v][i]
                visited.append(v)
                i = 0
            else:
                i += 1
