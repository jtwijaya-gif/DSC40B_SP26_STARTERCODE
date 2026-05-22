import dsc40graph

def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    original_call = biggest is None

    if biggest is None:
        biggest = {}

    curr_biggest = value[root]

    for neighbor in graph.neighbors(root):
        child_biggest = biggest_descendent(graph, neighbor, value, biggest)

        if child_biggest > curr_biggest:
            curr_biggest = child_biggest

    biggest[root] = curr_biggest

    if original_call:
        return biggest

    return curr_biggest