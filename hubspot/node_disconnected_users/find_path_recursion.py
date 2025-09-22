def find_path(connections, start, end, path):
    path = path + [start]
    if start == end:
        return path
    if start not in connections:
        return None
    for connection in connections[start]:
        if connection not in path:
            extended_path = find_path(connections, connection, end, path)
            if extended_path:
                return extended_path
    return None


def disconnected_users(net, users, source, crushes):
    if source in crushes:
        return sum(users.values())

    qty = 0
    new_net = [c for c in net if c[0] not in crushes and c[1] not in crushes]

    connections = {}
    for conn in new_net:
        for i in (0, 1):
            if conn[i] in connections:
                connections[conn[i]].append(conn[(i+1) % 2])
            else:
                connections[conn[i]] = [conn[(i+1) % 2]]

    for node in users:
        if find_path(connections, source, node, []) is None:
            qty += users[node]

    return qty
