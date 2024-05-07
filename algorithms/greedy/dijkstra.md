# Dijkstra's Algorithm

## Objective

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph

## Characteristics

- Relies on optimal substructure: any subgraph `B -> D` of the shortest path `A -> D` is also the shortest path between `B` and `D`

- Does not work for graphs with negative edges

## Algorithm

1. Set the initial distances for all vertices: 0 for the source vertex, and `inf` for the others

2. Choose the unvisited vertex with the shortest distance as the current vertex (this starts with the source vertex)

3. For each of the current vertex's unvisited neighbours, calculate the distance from the source and update the distance if the new distance is lower

4. After visiting all the neighbours, mark the vertex as visited (will not be checked again)

5. Repeat step 2 to choose a new current vertex

6. Repeat steps 3 - 4 until all vertices are marked as visited

7. This returns the shortest distance from the source vertex to every other vertex in the graph

```python
# Graph represented as adjacency matrix
class Graph:

    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [""] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # for undirected graphs - comment out for directed graphs

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, source_vertex):
        source_vertex_idx = self.vertex_data.index(source_vertex)
        distances = [float("inf")] * self.size
        distances[source_vertex_idx] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float("inf")
            u = None

            # choose the next vertex to visit
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            # update distances
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances
```

```python
g = Graph(7)

g.add_vertex_data(0, "A")
g.add_vertex_data(1, "B")
g.add_vertex_data(2, "C")
g.add_vertex_data(3, "D")
g.add_vertex_data(4, "E")
g.add_vertex_data(5, "F")
g.add_vertex_data(6, "G")

g.add_edge(3, 0, 4)  # D - A, weight 4
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

distances = g.dijkstra("D")

for idx, dist in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[idx]}: {dist}")
```

## Returning paths from Dijkstra's

- To return the actual path resulting in the shortest distances, we create a `predecessors` array to keep the previous vertex in the shortest path for each vertex

- This can be used to backtrack to find the shortest path for each vertex

```python
class Graph:
    # init methods (...)

    def dijkstra(self, source_vertex):
        source_vertex_idx = self.vertex_data.index(source_vertex)
        distances = [float("inf")] * self.size
        predecessors = [None] * self.size
        distances[source_vertex_idx] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float("inf")
            u = None

            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances, predecessors

    def get_path(self, predecessors, source_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)

        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]

            if current == self.vertex_data.index(source_vertex):
                path.insert(0, source_vertex)
                break

        return "->".join(path)

```

## Complexity Analysis

- Time Complexity: $O(\text{V}^2)$

    - Where $\text{V}$ is the number of vertices

    - The vertex with the lowest distance must be searched to choose the next current vertex $O(\text{V})$

    - This must be done for every vertex connected to the source $O(\text{V})$

- Space Complexity: $O(\text{V})$ to store the distances / predecessors for each vertex


## Resources

[Dijkstra's Overview](https://www.youtube.com/watch?v=_lHSawdgXpI)
