class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0] * vertices for _ in range(vertices)]
 
    def addEdge(self, u, v,dist):
        self.adjMatrix[u][v] = dist
        self.adjMatrix[v][u] = dist

    def all_paths(self, start, end):
        visited = [False] * self.vertices
        path = []
        paths = []
        self._find_all_paths(start, end, visited, path, paths)
        return paths

    def _find_all_paths(self, current, end, visited, path, paths):
        visited[current] = True
        path.append(current)

        if current == end:
            paths.append(path.copy())
        else:
            for neighbor in range(self.vertices):
                if self.adjMatrix[current][neighbor] >0 and not visited[neighbor]:
                    self._find_all_paths(neighbor, end, visited, path, paths)

        visited[current] = False
        path.pop()
        
        
    def dijkstra_with_path(self, src, dest):
        visited = [False] * self.vertices
        distance = [float('inf')] * self.vertices
        distance[src] = 0
        parent = [-1] * self.vertices

        for _ in range(self.vertices):
            # Find the vertex with the minimum distance value
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_vertex = v

            if min_vertex == -1:
                break

            visited[min_vertex] = True

            # Update the distance and parent of adjacent vertices
            for v in range(self.vertices):
                if self.adjMatrix[min_vertex][v] > 0 and not visited[v]:
                    new_distance = distance[min_vertex] + self.adjMatrix[min_vertex][v]
                    if new_distance < distance[v]:
                        distance[v] = new_distance
                        parent[v] = min_vertex

        # Reconstruct the shortest path
        path = []
        current = dest
        while current != -1:
            path.insert(0, current)
            current = parent[current]

        return distance[dest], path
def getsvals():

    Depart = clicked_depart.get()
    Destination = clicked_destin.get()
    Stations=["Mandi House","Bararkhamba Road","Rajiv Chowk","Patel Chowk","Central Secretariat","Udyog Bhawan",'Lok Kalyan Marg','Por Bagh',"Dilli Haat-INA","SouthExtension","Lajpat Nagar","Jangpura","Jawaharlal Nehru Stadium","Khan Market","Janpath"]

    n=15
    g = Graph(n)
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

    start_vertex=-1
    for i in range(len(Stations)):
        if Stations[i]==Depart:
            start_vertex=i
            break

        
    end_vertex=-1   
    for j in range(len(Stations)):
        if (Stations[j]==Destination):
            end_vertex=j
            break
    result_text.delete(1.0,END)

    paths = g.all_paths(start_vertex, end_vertex)
    
    
    result_text.insert(END,f"All paths between {Stations[start_vertex]} and {Stations[end_vertex]}:\n\n")
    for path in paths:
        for i in range(len(path)):
            if i==(len(path)-1):
                result_text.insert(END,f"{Stations[path[i]]}\n")
            else:
                result_text.insert(END,f"{Stations[path[i]]} -->")
        result_text.insert(END,'\n')

    shortest_distance, shortest_path = g.dijkstra_with_path(start_vertex, end_vertex)
    name=[Stations[node] for node in shortest_path]
    
    
    result_text.insert(END, "\n\n(Recommended)Shortest path:\n\n")
    result_text.insert(END, " --> ".join(name)+'\n\n')

    result_text.insert(END, f"Number of Stations = {len(shortest_path)-1}\n\n")
    result_text.insert(END, f"Shortest distance from {Depart} to {Destination} = {round(shortest_distance, 2)} Km\n\n")
    Time = shortest_distance / 0.4
    result_text.insert(END, f"Time Taken to reach from {Depart} to {Destination} = {round(Time, 2)} min\n")
    
    result_frame.grid(row=2, column=0, padx=7, pady=5)
    f1.grid_forget()
