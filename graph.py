def findAllShortestRoutesFrom(start: str, target: str = None, graph = None) -> tuple[dict[str, int], dict[str, list[str]], bool]:
    """Find the shortest route from a given station to all other stations"""
    graphKeys = list(graph.keys())
    if start not in graphKeys or (target is not None and target not in graphKeys):
        return None, None, False
    out = {start: 0}
    routes = {start: [start]}
    visited = [start]
    checked = []
    while len(checked) < len(graphKeys):  # Go through all stations
        recognised = 0
        for station in set(visited) - set(checked):  # Go through all visited stations that haven't been checked (length of the neighbors is not known)
            for neighbour in graph[station]:  # For each neighbour of a station
                if neighbour not in visited:  # If the neighbour hasn't been visited yet
                    out[neighbour] = out[station] + 1  # Add one to the distance to the neighbour (it can be reached in one stop)
                    visited.append(neighbour)  # Add to the list of visited, but unchecked stations
                    routes[neighbour] = routes[station] + [neighbour]  # Add to the route to get there
                    recognised += 1  # Add to the number of stations added this loop. If this is 0, then no new stations were added
            checked.append(station)  # Then mark the station as checked
            if target is not None and target in checked:  # If the target has been found, return
                return out, routes, False
        if recognised == 0:  # No stations have been added, so there is no route to the station
            return out, routes, True
        recognised = 0  # Reset the number of stations added
    return out, routes, False


def findShortestRouteBetween(start: str, end: str, data) -> tuple[int, list[str], bool]:
    """Returns shortest route (int), route (list[str]), and whether it failed (bool)"""
    shortestPaths, routes, failed = findAllShortestRoutesFrom(start, end, data)
    if failed:
        return None, None, True
    return shortestPaths[end], routes[end], False


def graphAll(data) -> dict[str, dict[str, int]]:
    out = {}
    for entry in data:
        out[entry] = findAllShortestRoutesFrom(entry, graph=data)[0]
    return out
