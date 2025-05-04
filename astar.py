import heapq
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions for moving the blank tile: (dx, dy)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def copy_state(state):
    return [row[:] for row in state]

def a_star(start):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start), 0, start, []))  # (f, g, state, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal_state:
            return path + [current]

        state_id = str(current)
        if state_id in visited:
            continue
        visited.add(state_id)

        x, y = find_blank(current)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                new_state = copy_state(current)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                if str(new_state) not in visited:
                    heapq.heappush(open_set, (
                        g + 1 + manhattan_distance(new_state), 
                        g + 1, 
                        new_state, 
                        path + [current]
                    ))
    return None

# Example initial state
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

# Run A* search
solution = a_star(initial_state)

# Print solution path and number of moves
if solution:
    print("Steps to solve the 8-puzzle:")
    for step in solution:
        for row in step:
            print(row)
        print()
    print("Total moves:", len(solution) - 1)
else:
    print("No solution found.")