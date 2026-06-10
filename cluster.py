def cluster(graph, weights, level):
    '''
    Clusters a graph based on similarity.
    '''
    visited = set()
    clusters = []

    for node in graph.nodes:
        if node not in visited:
            curr_cluster = set()
            stack = [node]
            visited.add(node)

            while stack:
                curr = stack.pop()
                curr_cluster.add(curr)

                for neighbor in graph.neighbors(curr):
                    if neighbor not in visited and weights(curr, neighbor) >= level:
                        visited.add(neighbor)
                        stack.append(neighbor)

            clusters.append(frozenset(curr_cluster))

    return frozenset(clusters)