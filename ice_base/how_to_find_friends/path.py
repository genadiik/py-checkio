def build_connections(network):
    connections = {}
    for conn in network:
        members = conn.split('-')
        for i in (0, 1):
            if members[i] in connections:
                connections[members[i]].append(members[(i+1) % 2])
            else:
                connections[members[i]] = [members[(i+1) % 2]]
    return connections


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


def check_connection(network, first, second):
    return find_path(build_connections(network), first, second, []) is not None
