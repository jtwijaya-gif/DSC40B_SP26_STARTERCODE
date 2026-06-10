def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    labels = {}

    for node in graph.nodes:
        if node not in labels:
            labels[node] = 'good'
            stack = [node]

            while stack:
                curr = stack.pop()

                if labels[curr] == 'good':
                    other = 'evil'
                else:
                    other = 'good'

                for neighbor in graph.neighbors(curr):
                    if neighbor not in labels:
                        labels[neighbor] = other
                        stack.append(neighbor)
                    elif labels[neighbor] == labels[curr]:
                        return None

    return labels