import heapq

#dijkstra
class Graph:
    def __init__(self, n):
        self.V = n
        self.adj = [[] for _ in range(n)]

    # Add nodes
    def connect(self, u, v, w=6):
        # Add an edge between nodes u and v with weight w (default is 6)
        self.adj[u].append((v, w))
        # Since the graph in undirected
        self.adj[v].append((u, w))

    # Function to perform Dijkstra's Algorithm that  
    # searches the smallest path
    def find_all_distances(self, src):
        # Priority queue to keep track of nodes to explore 
        pq = []
        # Start from the source node with distance node with distance 0
        heapq.heappush(pq, (0, src))
        # Initiaalize distances with infinity
        dist = [float('inf')]* self.V
        # Distance to the source node is 0
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                # If the distance is greater than the current known distance,
                # skip this node
                continue

            for v, w in self.adj[u]:
                # Update the distance if a shorter path is found
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        # Optional if you don't need the obvious value of 0
        dist.pop(src)
        # Prepare the result as a list of string
        result = [str(d) if d != float('inf') else '-1' for d in dist]
        print(' '.join(result))   

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)