goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]
# Manhattan Distance Heuristic
def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i = (val - 1) // 3
                goal_j = (val - 1) % 3
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

# Find the blank (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighboring states
def get_neighbors(state):
    x, y = find_zero(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm (simple list instead of heapq)
def a_star(start):
    open_set = [(start, 0, [start])]  # (state, cost, path)
    visited = []

    while open_set:
        # Find the state with the lowest f = g + h
        best_index = 0
        best_f = open_set[0][1] + heuristic(open_set[0][0])

        for i, (state, g, path) in enumerate(open_set):
            f = g + heuristic(state)
            if f < best_f:
                best_index = i
                best_f = f

        current, g, path = open_set.pop(best_index)

        if current == goal:
            print("Solved in", g, "moves\n")
            print("Steps:")
            for step in path:
                for row in step:
                    print(row)
                print()
            return

        if current in visited:
            continue
        visited.append(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                open_set.append((neighbor, g + 1, path + [neighbor]))

    print("No solution.")

# Example start state
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

a_star(start_state)