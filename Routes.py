import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes

def shortest_path(previous_nodes, destination):
    path = []
    current_node = destination
    while current_node:
        path.insert(0, current_node)
        current_node = previous_nodes.get(current_node)
    return path

# Sample graph of railway distances in kilometers
graph = {
    "Borno": {
        "Gombe": 290,
        "Plateau": 420,
        "Kaduna": 580
    },
    "Gombe": {
        "Plateau": 565,
        "Yobe": 760
    },
    "Plateau": {
        "Yobe": 390,
        "Kaduna": 180
    },
    "Kaduna": {
        "Yobe": 520
    },
    "Yobe": {
        "Borno": 580
    }
    
}

# Travel time measurement: 1 kilometer = 20 minutes
time_per_km = 20

# Display available terminals to choose from
print("Available terminals:", ", ".join(graph.keys()))

while True:
    start_location = input("Enter starting location: ")
    if start_location in graph:
        break
    else:
        print("Invalid location. Please choose from the available terminals.")

while True:
    destination = input("Enter destination: ")
    if destination in graph:
        break
    else:
        print("Invalid location. Please choose from the available terminals.")

distances, previous_nodes = dijkstra(graph, start_location)
shortest_dist = distances[destination]
estimated_time = shortest_dist * time_per_km

# Convert time to hours if greater than or equal to 60 minutes
if estimated_time >= 60:
    estimated_hours = estimated_time // 60
    estimated_minutes = estimated_time % 60
    estimated_time_formatted = f"{estimated_hours} hrs {estimated_minutes} mins"
else:
    estimated_time_formatted = f"{estimated_time} mins"

shortest_path_nodes = shortest_path(previous_nodes, destination)

print(f"Shortest distance from {start_location} to {destination}: {shortest_dist} km")
print(f"Estimated travel time: {estimated_time_formatted}")
print("Shortest path:", " -> ".join(shortest_path_nodes))
