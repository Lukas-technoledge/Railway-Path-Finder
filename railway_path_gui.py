import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import heapq

# The rest of your code for Dijkstra's algorithm and shortest path function
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


def calculate_shortest_path():
    start_location = start_combobox.get()
    destination = destination_combobox.get()

    if start_location == destination:
        messagebox.showinfo("Error", "Start and destination cannot be the same.")
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

    result_label.config(text=f"Shortest distance: {shortest_dist} km\nEstimated travel time: {estimated_time_formatted}\nShortest path: {' -> '.join(shortest_path_nodes)}")

# Create GUI window
root = tk.Tk()
root.title("Railway Path Finder")

# Create and place widgets
start_label = ttk.Label(root, text="Select starting location:")
start_label.pack()

start_combobox = ttk.Combobox(root, values=list(graph.keys()))
start_combobox.pack()

destination_label = ttk.Label(root, text="Select destination:")
destination_label.pack()

destination_combobox = ttk.Combobox(root, values=list(graph.keys()))
destination_combobox.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_shortest_path)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

# Run the GUI loop
root.mainloop()
