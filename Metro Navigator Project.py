# Graph class to store metro stations and distances
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # Create adjacency matrix initialized with 0
        self.adjMatrix = [[0] * vertices for _ in range(vertices)]
 
    # Add an edge (undirected graph)
    def addEdge(self, u, v, dist):
        self.adjMatrix[u][v] = dist
        self.adjMatrix[v][u] = dist

    # Find all possible paths between two stations
    def all_paths(self, start, end):
        visited = [False] * self.vertices
        path = []
        paths = []
        self._find_all_paths(start, end, visited, path, paths)
        return paths

    # Helper function using DFS to generate paths
    def _find_all_paths(self, current, end, visited, path, paths):
        visited[current] = True
        path.append(current)

        # If reached destination, save the path
        if current == end:
            paths.append(path.copy())
        else:
            # Explore neighbors
            for neighbor in range(self.vertices):
                if self.adjMatrix[current][neighbor] > 0 and not visited[neighbor]:
                    self._find_all_paths(neighbor, end, visited, path, paths)

        # Backtrack
        visited[current] = False
        path.pop()
        
        
    # Dijkstra algorithm to find shortest path
    def dijkstra_with_path(self, src, dest):
        visited = [False] * self.vertices
        distance = [float('inf')] * self.vertices
        distance[src] = 0
        parent = [-1] * self.vertices

        for _ in range(self.vertices):
            # Select vertex with minimum distance
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited[min_vertex] = True

            # Update distances to neighbors
            for v in range(self.vertices):
                if self.adjMatrix[min_vertex][v] > 0 and not visited[v]:
                    new_distance = distance[min_vertex] + self.adjMatrix[min_vertex][v]
                    if new_distance < distance[v]:
                        distance[v] = new_distance
                        parent[v] = min_vertex

        # Reconstruct shortest path
        path = []
        current = dest
        while current != -1:
            path.insert(0, current)
            current = parent[current]

        return distance[dest], path


# Function triggered when user presses "Search"
def getsvals():

    # Get selected stations from dropdown
    Depart = clicked_depart.get()
    Destination = clicked_destin.get()

    # List of metro stations
    Stations = [
        "Mandi House","Bararkhamba Road","Rajiv Chowk","Patel Chowk",
        "Central Secretariat","Udyog Bhawan",'Lok Kalyan Marg','Por Bagh',
        "Dilli Haat-INA","SouthExtension","Lajpat Nagar","Jangpura",
        "Jawaharlal Nehru Stadium","Khan Market","Janpath"
    ]

    # Create graph with 15 nodes
    n = 15
    g = Graph(n)

    # Add metro station connections with distances
    g.addEdge(0,1,1.1)
    g.addEdge(1,2,0.6)
    g.addEdge(2,3,1.2)
    g.addEdge(3,4,0.8)
    g.addEdge(4,5,0.6)
    g.addEdge(5,6,1.4)
    g.addEdge(6,7,1.3)
    g.addEdge(7,8,1.3)
    g.addEdge(8,9,1.3)
    g.addEdge(9,10,1.8)
    g.addEdge(10,11,1.5)
    g.addEdge(11,12,0.9)
    g.addEdge(12,13,1.7)
    g.addEdge(13,4,2.4)
    g.addEdge(14,0,1.9)
    g.addEdge(14,4,1.3)

    # Convert selected station names to indices
    start_vertex = Stations.index(Depart)
    end_vertex = Stations.index(Destination)

    # Clear text box
    result_text.delete(1.0, END)

    # Get all possible paths
    paths = g.all_paths(start_vertex, end_vertex)
    
    # Print all paths
    result_text.insert(END, f"All paths between {Stations[start_vertex]} and {Stations[end_vertex]}:\n\n")
    for path in paths:
        for i in range(len(path)):
            if i == len(path) - 1:
                result_text.insert(END, f"{Stations[path[i]]}\n")
            else:
                result_text.insert(END, f"{Stations[path[i]]} -->")
        result_text.insert(END, '\n')

    # Shortest path using Dijkstra
    shortest_distance, shortest_path = g.dijkstra_with_path(start_vertex, end_vertex)
    name = [Stations[node] for node in shortest_path]
    
    result_text.insert(END, "\n\n(Recommended)Shortest path:\n\n")
    result_text.insert(END, " --> ".join(name) + '\n\n')

    # Display stats
    result_text.insert(END, f"Number of Stations = {len(shortest_path) - 1}\n\n")
    result_text.insert(END, f"Shortest distance from {Depart} to {Destination} = {round(shortest_distance, 2)} Km\n\n")

    # Assuming average speed 0.4 km/min (~24 km/h)
    Time = shortest_distance / 0.4
    result_text.insert(END, f"Time Taken = {round(Time, 2)} min\n")
    
    # Show result frame
    result_frame.grid(row=2, column=0, padx=7, pady=5)
    f1.grid_forget()


# ---------------- Tkinter UI ----------------

from tkinter import *
from PIL import ImageTk, Image  

root = Tk()
root.geometry("800x780")
root.maxsize(800, 780)
root.title("Metro Navigator")
root.config(background="#333333")
root.wm_iconbitmap("assests\metro.ico")

# Load image banner
image = Image.open("assests\pexels-pixabay-302428 (2).jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, width=750, height=290)
label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Title text
l1 = Label(
    text="Travel More, Worry Less", bg="#333333", fg="#FFD858",
    padx=40, pady=50, font="Helvetica 24 bold"
)
l1.grid(row=1, column=0, columnspan=2)

# Input frame
f1 = Frame(root, bg="#333333")
f1.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

# Labels
Depart = Label(f1, text="Depart From:", fg="#FFD858", bg="#333333", font="Helvetica 16 bold")
Depart.grid(row=0, column=0, padx=7, pady=5)

Destination = Label(f1, text="Destination:", fg="#FFD858", bg="#333333", font="Helvetica 16 bold")
Destination.grid(row=1, column=0, padx=7, pady=7)

# Dropdown station list
options = [
    "Mandi House", "Bararkhamba Road", "Rajiv Chowk", "Patel Chowk",
    "Central Secretariat", "Udyog Bhawan", 'Lok Kalyan Marg', 'Por Bagh',
    "Dilli Haat-INA", "South Extension", "Lajpat Nagar", "Jangpura",
    "Jawaharlal Nehru Stadium", "Khan Market", "Janpath"
]

# Departure dropdown
clicked_depart = StringVar()
clicked_depart.set(options[0])
Depart_drop = OptionMenu(f1, clicked_depart, *options)
Depart_drop.config(bg="#333333", fg="#FFD858", highlightthickness=0)
Depart_drop.grid(row=0, column=1, padx=7, pady=5)

# Destination dropdown
clicked_destin = StringVar()
clicked_destin.set(options[0])
Destin_drop = OptionMenu(f1, clicked_destin, *options)
Destin_drop.config(bg="#333333", fg="#FFD858", highlightthickness=0)
Destin_drop.grid(row=1, column=1, padx=7, pady=5)


# Button hover effects
def on_hover(event):
    b1.config(bg="white")

def on_leave(event):
    b1.config(bg="#FFD858")

# Search button
b1 = Button(
    f1, bg="#FFD858", fg="#333333", text="Search",
    command=getsvals, font="Helvetica 16 bold",
    padx=10, pady=5, relief=SUNKEN, borderwidth=5
)
b1.grid(row=2, column=0, columnspan=2, padx=100, pady=40)
b1.bind("<Enter>", on_hover)
b1.bind("<Leave>", on_leave)

# Frame where results appear
result_frame = Frame(root, bg="#333333")
result_frame.grid(row=3, column=0, columnspan=2, padx=50, pady=10, sticky="w")
result_frame.grid_forget()

# Result text box
result_text = Text(result_frame, height=10, width=60, font='Helvetica 12', bg="#FFD858")
result_text.pack(padx=70, pady=20)

root.mainloop()
