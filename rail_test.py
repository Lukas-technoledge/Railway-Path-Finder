import heapq
import tkinter as tk
from tkinter import messagebox

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
time_per_km = 0.6

# Create GUI window
root = tk.Tk()
root.title("Railway Route Planner")

# Display available terminals to choose from
terminal_label = tk.Label(root, text="Available terminals: " + ", ".join(graph.keys()))
terminal_label.pack()

# Entry fields for start location and destination
start_label = tk.Label(root, text="Enter starting location:")
start_label.pack()
start_entry = tk.Entry(root)
start_entry.pack()

destination_label = tk.Label(root, text="Enter destination:")
destination_label.pack()
destination_entry = tk.Entry(root)
destination_entry.pack()

# Function to calculate shortest path and display result
def calculate_shortest_path():
    start_location = start_entry.get()
    destination = destination_entry.get()

    if start_location not in graph or destination not in graph:
        messagebox.showerror("Error", "Invalid location. Please choose from the available terminals.")
        return

    distances, previous_nodes = dijkstra(graph, start_location)
    shortest_dist = distances[destination]
    estimated_time = shortest_dist * time_per_km

    if estimated_time >= 60:
        estimated_hours = estimated_time // 60
        estimated_minutes = estimated_time % 60
        estimated_time_formatted = f"{estimated_hours} hrs {estimated_minutes} mins"
    else:
        estimated_time_formatted = f"{estimated_time} mins"

    shortest_path_nodes = shortest_path(previous_nodes, destination)

    result_label.config(text=f"Shortest distance from {start_location} to {destination}: {shortest_dist} km\n"
                             f"Estimated travel time: {estimated_time_formatted}\n"
                             f"Shortest path: {' -> '.join(shortest_path_nodes)}")

# Button to calculate and display result
calculate_button = tk.Button(root, text="Calculate", command=calculate_shortest_path)
calculate_button.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start GUI event loop
root.mainloop()
