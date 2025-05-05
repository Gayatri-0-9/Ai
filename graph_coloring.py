graph = {}
n = int(input("Enter number of edges: "))
print("Enter edges as two letters like AB:")

# Step 1: Read edges and build graph
for i in range(n):
    edge = input(f"Edge {i+1}: ")
    u = edge[0]
    v = edge[1]
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# Step 2: Prepare color list and assignments
colors = ["red", "green", "blue", "yellow", "brown"]
colorsassigned = {}

# Step 3: Assign colors using simple greedy approach
for node in graph:
    used_colors = set()
    for neighbor in graph[node]:
        if neighbor in colorsassigned:
            used_colors.add(colorsassigned[neighbor])
    # Assign the first color that is not used
    for color in colors:
        if color not in used_colors:
            colorsassigned[node] = color
            break

# Step 4: Show result
print("\nGraph coloring result:")
for node in colorsassigned:
    print(f"{node} -> {colorsassigned[node]}")