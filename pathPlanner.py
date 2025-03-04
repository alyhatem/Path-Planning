def do_a_star(grid, start, end, display_message):
    # Helper function for Euclidean distance
    def euclid(a, b):
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    
    # Helper function to reconstruct the path
    def reconstruct_path(node):
        path = []
        while node:
            path.append(node)
            node = parents.get(node)
        return path[::-1]
    
    # Directions: right, left, down, up
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Open and closed sets
    open_list = [start]
    closed_list = set()
    parents = {}
    g_score = {start: 0}
    f_score = {start: euclid(start, end)}
    
    while open_list:
        # Get node with the lowest f-score
        current = min(open_list, key=lambda x: f_score.get(x, float('inf')))
        
        if current == end:
            return reconstruct_path(current)
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if neighbor in closed_list:
                continue
            
            # Check bounds and if it's walkable
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1:
                tentative_g = g_score[current] + 1

                if neighbor not in open_list:
                    open_list.append(neighbor)
                elif tentative_g >= g_score[neighbor]:
                    continue
                
                parents[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + euclid(neighbor, end)
        
        open_list.remove(current)
        closed_list.add(current)
    
    return []  # No path found

#end of file