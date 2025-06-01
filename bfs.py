from collections import deque
# N.B- We know that, Breadt-First-Search uses FIFO(First-In-First-Out)

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start, goal):
    frontier = deque([start]) # Initialize the frontier with the start node
    came_from = {start: None} # Remember where we came from for each node(basically to rebuild the path)

    #Now, we have to keep checking until there is nothing left in the queue
    while frontier:
        current = frontier.popleft() # We take the first node form the queue 
        print(f"Visiting {current}")

        # Another important step: If we have found the goal, we stop!
        if(current == goal):
            print("Goal Found!")
            break

        # Now, we considering the kids, basically(The children of the current node).
        for kid in graph[current]:
            if kid not in came_from: # If we have not visited it.
                frontier.append(kid) # now, becomes the frontier, added to queue
                came_from[kid] = current # Record how we got there
    
    # Rebuilding the path from start to goal
    if goal in came_from:
        path = []
        while goal is not None:
            path.append(goal)
            goal = came_from[goal]
        path.reverse()
        return path
    else:
        return None

path = bfs(graph,'A','G')

print(f"shortest path {path}")


