# Min-Heap implementation
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Add new item and maintain heap property."""
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the smallest element (lowest f-score)."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._bubble_down(0)
        return root

    def update_priority(self, node, new_f):
        """Update priority if new f_score is lower."""
        for i in range(len(self.heap)):
            if self.heap[i][1] == node:  # Find node
                if new_f < self.heap[i][0]:  # Only update if lower f_score
                    self.heap[i] = (new_f, node)
                    self._bubble_up(i)
                break

    def _bubble_up(self, index):
        """Move element up to maintain heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Move element down to maintain heap property."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == index:
                break  # No more swapping needed
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0


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
    open_list = MinHeap()
    closed_list = set()
    parents = {}
    g_score = {start: 0}
    f_score = {start: euclid(start, end)}
    open_list.push((f_score[start], start))  # Push initial node
    open_dict = {start: euclid(start, end)}  # Dictionary for lookup

    while open_list:
        # Get node with the lowest f-score
        current = open_list.pop()[1]  # Extract node with lowest f-score
        
        if current == end:
            return reconstruct_path(current)
        
        open_dict.pop(current)
        closed_list.add(current)
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if neighbor in closed_list:
                continue
            
            # Check bounds and if it's walkable
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1:
                tentative_g = g_score[current] + 1
                tentative_f = tentative_g + euclid(neighbor, end)

                if neighbor not in open_dict:
                    open_list.push((tentative_f, neighbor))
                    open_dict[neighbor] = tentative_f
                    parents[neighbor] = current
                elif tentative_g >= g_score[neighbor]:
                    continue

                parents[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_f

    return []  # No path found
# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1],
#     [0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]

# start = (0, 0)  # Top-left corner
# end = (4, 4)    # Bottom-right corner

# path = do_a_star(grid, start, end)
# print("Path found:", path)

#end of file