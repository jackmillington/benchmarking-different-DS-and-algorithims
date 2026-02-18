def simple_dijkstra(graph, start, end, weight_type='distance', alpha=1.0, beta=1.0):

    # Each element: (current_cost, current_node, path_so_far)
    queue = [(0, start, [start])]
    visited = {}

    while queue:
        # Find the entry with the lowest cost
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        cost, node, path = queue.pop(min_index)

        if node == end:
            return cost, path

        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost

        for neighbor, dist in graph[node]['roads'].items():
            toll = graph[neighbor]['toll']
            if weight_type == 'distance':
                total_cost = cost + dist
            elif weight_type == 'toll':
                total_cost = cost + toll
            elif weight_type == 'balanced':
                total_cost = cost + alpha * dist + beta * toll
            else:
                total_cost = cost + dist  # default to distance
            if neighbor not in path:  # avoid cycles
                queue.append((total_cost, neighbor, path + [neighbor]))
    return float('inf'), []

def filter_routes(routes):
    """Pareto filtering as before."""
    non_dominated = []
    for r in routes:
        dist, toll, path = r
        dominated = False
        for other in routes:
            odist, otoll, _ = other
            if (odist <= dist and otoll <= toll) and (odist < dist or otoll < toll):
                dominated = True
                break
        if not dominated:
            non_dominated.append(r)
    return non_dominated

def route_selection_system(Map, start, end):
    # Shortest by distance
    dist_cost, dist_path = simple_dijkstra(Map, start, end, weight_type='distance')
    dist_toll = sum(Map[n]['toll'] for n in dist_path)
    
    # Most cost-effective by toll
    toll_cost, toll_path = simple_dijkstra(Map, start, end, weight_type='toll')
    toll_dist = sum(Map[toll_path[i]]['roads'][toll_path[i+1]] for i in range(len(toll_path)-1)) if len(toll_path)>1 else 0
    
    # Balanced: try alpha=1, beta=1
    bal_cost, bal_path = simple_dijkstra(Map, start, end, weight_type='balanced', alpha=1, beta=1)
    bal_dist = sum(Map[bal_path[i]]['roads'][bal_path[i+1]] for i in range(len(bal_path)-1)) if len(bal_path)>1 else 0
    bal_toll = sum(Map[n]['toll'] for n in bal_path)

    # Balanced: try alpha=2, beta=1
    bal_cost2, bal_path2 = simple_dijkstra(Map, start, end, weight_type='balanced', alpha=2, beta=1)
    bal_dist2 = sum(Map[bal_path[i]]['roads'][bal_path[i+1]] for i in range(len(bal_path)-1)) if len(bal_path)>1 else 0
    bal_toll2 = sum(Map[n]['toll'] for n in bal_path)

    # Balanced: try alpha=1, beta=2
    bal_cost3, bal_path3 = simple_dijkstra(Map, start, end, weight_type='balanced', alpha=1, beta=2)
    bal_dist3 = sum(Map[bal_path[i]]['roads'][bal_path[i+1]] for i in range(len(bal_path)-1)) if len(bal_path)>1 else 0
    bal_toll3 = sum(Map[n]['toll'] for n in bal_path)
    
    # Collect all route options
    routes = [
        (dist_cost, dist_toll, dist_path),
        (toll_dist, toll_cost, toll_path),
        (bal_dist, bal_toll, bal_path),
        (bal_dist2, bal_toll2, bal_path2),
        (bal_dist3, bal_toll3, bal_path3)
    ]

    # Remove exact duplicate routes (optional)
    unique_routes = []
    seen = set()
    for r in routes:
        key = (tuple(r[2]), r[0], r[1])  # use route path, distance, and toll as key
        if key not in seen:
            seen.add(key)
            unique_routes.append(r)

    
    # Filter as before
    filtered = filter_routes(unique_routes)
    for i, (dist, toll, path) in enumerate(filtered):
        print(f"Option {i+1}: Route {path} - Total distance: {dist}, Total toll: {toll}")
    return filtered

# Example Map
Map = {
    "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
    "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
    "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
    "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
    "E": {"toll": 5, "roads": {"C": 6, "D": 2}}
}

# Run the system
route_selection_system(Map, "A", "E")
