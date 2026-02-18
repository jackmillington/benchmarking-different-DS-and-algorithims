# def dijkstrasAlgo(graph, start, end, weightType = 'distance', distWeight = 1.0, tollWeight = 1.0):

#     # initialises all weights to infinity except the start
#     weights = {}
#     for node in graph:
#         weights[node] = float('inf')
#     weights[start] = 0

#     # initialises previous dictionary
#     # {"A": None, "B": None, etc}  
#     previous = {}
#     for node in graph:
#         previous[node] = None
    
#     # creates a set {"A", "B", etc}
#     unvisited = set(graph.keys())

#     while unvisited: # while there are still unvisited nodes 
#         current = None
#         for node in unvisited: # loops through all unvisited and finds node with least weight
#             if current is None or weights[node] < weights[current]:
#                 current = node
        
#         if current == end: # if node is the end node, stop
#             break

#         # visits all neighbours of current node
#         for neighbor, distance in graph[current]["roads"].items():
#             if neighbor in unvisited:
#                 toll = graph[neighbor]["toll"]
#                 if weightType == 'distance':
#                     # find distance from start to this neighbour 
#                     newWeight = weights[current] + distance
#                 if weightType == 'toll':
#                     # find toll from start to this neighbour 
#                     newWeight = weights[current] + toll
#                 if weightType == 'balance':
#                     # find distance and toll from start to this neighbour weighted accordingly
#                     newWeight = weights[current] + (distance*distWeight + toll*tollWeight)
                    
                
#                 # if it is the shortest found so far, update record in weights
#                 #  and record we came from current
#                 if newWeight < weights[neighbor]:
#                         weights[neighbor] = newWeight
#                         previous[neighbor] = current

#         unvisited.remove(current) # mark as visited and repeat for all nodes

#     # reconstruct path
#     path = []
#     current = end # start at end node
#     while current is not None:
#         path.insert(0, current) # inserts to front of path list to keep in forward order
#         current = previous[current]

#     # if the start isnt reached then there is no path
#     if weights[end] == float('inf'):
#         return None, []
    
#     return path # returns a weight and the path it took

# def calcDistAndToll(graph, path):
#     dist = 0
#     toll = 0
#     for i in range(len(path)):
#         node = path[i]
#         toll += graph[node]['toll']
#         if i > 0:
#             prev = path[i - 1]
#             dist += graph[prev]['roads'][node]
#     return dist, toll, path

# def printOptions(graph, start, stop):
#     options = []
#     dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'distance'))
#     options.append((dist, toll, path))
#     dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'toll'))
#     options.append((dist, toll, path))
#     dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 1, 1))
#     options.append((dist, toll, path))
#     dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 2, 1))
#     options.append((dist, toll, path))
#     dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 1, 2))
#     options.append((dist, toll, path))
    
#     result = filterOptions(options)
#     i = 0
#     for dist, toll, path in result:
#         i+=1
#         print(f"Option {i}: distance: {dist}, toll: {toll}, Path is {path}")
#     return

# def filterOptions(options):
#     # first, filter for duplicates
#     seen = set()
#     filtered = []
#     for dist, toll, path in options:
#         # set as tuple so it can be put in set
#         pathTuple = tuple(path)
#         if pathTuple not in seen:
#             filtered.append((dist, toll, path))
#             seen.add(pathTuple)

#     # Then delete any paths that are both longer and cost more than another
#     good = []
#     for i, (dist_i, toll_i, path_i) in enumerate(filtered):
#         worse = False
#         for j, (dist_j, toll_j, path_j) in enumerate(filtered):
#             if i == j:
#                 continue
#         if (dist_i >= dist_j and toll_i >= toll_j) and (dist_i > dist_j or toll_i > toll_j):
#             worse = True
#             break
#         if not worse:
#             good.append((dist_i, toll_i, path_i))   

#     return good


    

    

# # road network modelled as a graph
# roadNetwork = {
#     "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
#     "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
#     "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
#     "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
#     "E": {"toll": 5, "roads": {"C": 6, "D": 2}}
# }

# # example usage
# printOptions(roadNetwork, "A", "E")
        

def dijkstrasAlgo(graph, start, end, weightType = 'distance', distWeight = 1.0, tollWeight = 1.0):

    # initialises all weights to infinity except the start
    weights = {}
    for node in graph:
        weights[node] = float('inf')
    weights[start] = 0

    # initialises previous dictionary
    # {"A": None, "B": None, etc}  
    previous = {}
    for node in graph:
        previous[node] = None
    
    # creates a set {"A", "B", etc}
    unvisited = set(graph.keys())

    while unvisited: # while there are still unvisited nodes 
        current = None
        for node in unvisited: # loops through all unvisited and finds node with least weight
            if current is None or weights[node] < weights[current]:
                current = node
        
        if current == end: # if node is the end node, stop
            break

        # visits all neighbours of current node
        for neighbor, distance in graph[current]["roads"].items():
            if neighbor in unvisited:
                toll = graph[neighbor]["toll"]
                if weightType == 'distance':
                    # find distance from start to this neighbour 
                    newWeight = weights[current] + distance
                if weightType == 'toll':
                    # find toll from start to this neighbour 
                    newWeight = weights[current] + toll
                if weightType == 'balance':
                    # find distance and toll from start to this neighbour weighted accordingly
                    newWeight = weights[current] + (distance*distWeight + toll*tollWeight)
                    
                
                # if it is the shortest found so far, update record in weights
                #  and record we came from current
                if newWeight < weights[neighbor]:
                        weights[neighbor] = newWeight
                        previous[neighbor] = current

        unvisited.remove(current) # mark as visited and repeat for all nodes

    # reconstruct path
    path = []
    current = end # start at end node
    while current is not None:
        path.insert(0, current) # inserts to front of path list to keep in forward order
        current = previous[current]

    # if the start isnt reached then there is no path
    if weights[end] == float('inf'):
        return None, []
    
    return path # returns a weight and the path it took

def calcDistAndToll(graph, path):
    dist = 0
    toll = 0
    for i in range(len(path)):
        node = path[i]
        toll += graph[node]['toll']
        if i > 0:
            prev = path[i - 1]
            dist += graph[prev]['roads'][node]
    return dist, toll, path

def printOptions(graph, start, stop):
    options = []
    dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'distance'))
    options.append((dist, toll, path))
    dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'toll'))
    options.append((dist, toll, path))
    dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 1, 1))
    options.append((dist, toll, path))
    dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 2, 1))
    options.append((dist, toll, path))
    dist, toll, path = calcDistAndToll(graph, dijkstrasAlgo(graph, start, stop, 'balance', 1, 2))
    options.append((dist, toll, path))
    
    result = filterOptions(options)
    i = 0
    for dist, toll, path in result:
        i+=1
        print(f"Option {i}: distance: {dist}, toll: {toll}, Path is {path}")
    return

def filterOptions(options):
    # first, filter for duplicates
    seen = set()
    filtered = []
    for dist, toll, path in options:
        # set as tuple so it can be put in set
        pathTuple = tuple(path)
        if pathTuple not in seen:
            filtered.append((dist, toll, path))
            seen.add(pathTuple)

    # Then delete any paths that are both longer and cost more than another
    good = []
    for i, (dist_i, toll_i, path_i) in enumerate(filtered):
        worse = False
        for j, (dist_j, toll_j, path_j) in enumerate(filtered):
            if i == j:
                continue
        if (dist_i >= dist_j and toll_i >= toll_j) and (dist_i > dist_j or toll_i > toll_j):
            worse = True
            break
        if not worse:
            good.append((dist_i, toll_i, path_i))   

    return good


    

    

# road network modelled as a graph
roadNetwork = {
    "A": {"toll": 0, "roads": {"B": 4, "C": 8}},
    "B": {"toll": 2, "roads": {"A": 4, "C": 2, "D": 5}},
    "C": {"toll": 3, "roads": {"A": 8, "B": 2, "D": 3, "E": 6}},
    "D": {"toll": 2, "roads": {"B": 5, "C": 3, "E": 2}},
    "E": {"toll": 5, "roads": {"C": 6, "D": 2}}
}

# example usage
printOptions(roadNetwork, "A", "E")
        
