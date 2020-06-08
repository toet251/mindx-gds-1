def ex4(n, dislikes):
    # group_index only in [1,2]
    def BFS(i, group, next, group_index):
        # BFS to index group for node
        group[i] = group_index
        
        queue = []
        queue.append((i, group_index))

        while len(queue):
            u, group_u = queue.pop(0)
            not_group_u = 3 - group_u
            for v in next[u]:
                if not group[v]:
                    group[v] = not_group_u
                    queue.append((v, group[v]))
                else:
                    if group[v] != not_group_u:
                        return False

        return True
        
    group = [0] * (n+1)
    next = [[] for _ in range(n+1)]

    # Build edges
    for edge in dislikes:
        u, v = edge
        next[u].append(v) 
        next[v].append(u)

    # BFS to index group for each node
    for i in range(1, n+1):
        if group[i]:
            continue
        
        check = BFS(i, group, next, 0)
        if not check:
            return False

    return True

# print(ex4(4, [[1,2],[1,3],[2,4]]))
# print(ex4(3, [[1,2],[1,3],[2,3]]))
# print(ex4(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
