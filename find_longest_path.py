import igraph as ig

#This function finds the longest simple path in a graph by looping through a list of all simple paths and returns the length of the longest path 
def find_longest_path(g):
    path_set = []

    for i in range(len(g.vs)):
        path_set = path_set + g.get_all_simple_paths(g.vs[i]) #function from igraph

    longest = 0
    longest_path = []
    for i in range(len(path_set)):
        if len(path_set[i]) > longest:
            longest = len(path_set[i])
            longest_path = path_set[i]

    if longest == 0:
        return 0, longest_path
    else:
        return longest - 1, longest_path
    
