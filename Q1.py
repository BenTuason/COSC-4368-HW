import sys
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, src, destination):
        pq = []
        heapq.heappush(pq, (0, src))

        dist = [sys.maxsize] * self.V
        dist[src] = 0

        parent = [-1] * self.V

        while pq:
            current_dist, u = heapq.heappop(pq)

            if u == destination:
                break

            for neighbor, weight in self.graph[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    parent[neighbor] = u  # Track the path
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        if dist[destination] == sys.maxsize:
            print(f"No path found from {src} to {destination}")
            return None, None

        total_cost = dist[destination]
        path = self.get_path(parent, destination)

        return path, total_cost

    def get_path(self, parent, destination):
        path = []
        while destination != -1:
            path.append(destination)
            destination = parent[destination]
        path.reverse()
        return path

    def dfs_util(self, src, destination, visited, path, path_cost, min_path, min_cost):
        visited[src] = True
        path.append(src)

        if src == destination:
            if path_cost < min_cost[0]:
                min_cost[0] = path_cost
                min_path[0] = list(path)
        else:
            for neighbor, weight in self.graph[src]:
                if not visited[neighbor]:
                    self.dfs_util(neighbor, destination, visited, path, path_cost + weight, min_path, min_cost)

        path.pop()
        visited[src] = False

    def dfs_shortest_path(self, src, destination):
        visited = [False] * self.V
        min_path = [[]]
        min_cost = [float('inf')]
        self.dfs_util(src, destination, visited, [], 0, min_path, min_cost)

        if min_path[0]:
            return min_path[0], min_cost[0]
        else:
            return None, None

if __name__ == "__main__":
    g = Graph(8)

    g.add_edge(0, 1, 2)
    g.add_edge(1, 0, 1)
    g.add_edge(0, 3, 2)
    g.add_edge(3, 0, 1)
    g.add_edge(0, 7, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 4, 4)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 5, 7)
    g.add_edge(4, 5, 5)
    g.add_edge(4, 6, 4)
    g.add_edge(5, 6, 2)
    g.add_edge(7, 4, 4)
    g.add_edge(7, 5, 6)

    destinations = [7, 5, 6]

    for dest in destinations:
        print(f"Finding shortest path from 0 to {dest}...\n")

        print("BFS/Dijkstra's result:")
        dijkstra_path, dijkstra_cost = g.dijkstra(0, dest)
        if dijkstra_path is not None:
            print(f"Path: {dijkstra_path}")
            print(f"Total Cost: {dijkstra_cost}")
        else:
            print(f"No path found using Dijkstra from 0 to {dest}")

        print()

        print("DFS result:")
        dfs_path, dfs_cost = g.dfs_shortest_path(0, dest)
        if dfs_path is not None:
            print(f"Path: {dfs_path}")
            print(f"Total Cost: {dfs_cost}")
        else:
            print(f"No path found using DFS from 0 to {dest}")

        print("\n" + "-" * 30 + "\n")
