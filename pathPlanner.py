# Min-Heap priority queue implementation for efficient retrieval of nodes with the lowest f-score
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Add new node and maintain heap property."""
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """Extract the node with the minimum f-score from the open list."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, index):
        """Move node up to maintain heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Move node down to maintain heap property."""
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
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

# A* Pathfinding algorithm implementation to find optimal path to goal node
def do_a_star(grid, start, end, display_message):
    # Euclidean heuristic function (h(n)), ensures admissibility and consistency
    def euclid(a, b):
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

    # Reconstruct optimal path by backtracking through parent pointers
    def reconstruct_path(node):
        path = []
        while node:
            path.append(node)
            node = predecessors.get(node)
        return path[::-1]  # Reverse path to start-to-goal order

    # Cardinal directions representing permissible moves (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    open_list = MinHeap()  # Open list (nodes to explore)
    closed_list = set()    # Nodes already expanded
    predecessors = {}  # To reconstruct optimal path upon reaching goal node

    g_score = {start: 0}  # g(n): Actual minimum cost from the start node to node n
    f_score = {start: euclid(start, end)}  # f(n): Evaluation function, f = g + h

    open_list.push((f_score[start], start)) # Mark start node 's' as open
    open_set = {start}  # For efficient lookup

    while open_list.heap:
        # Node selection based on lowest evaluation function value (f-score)
        current = open_list.pop()[1]

        # Termination condition: reached the goal node
        if current == end:
            return reconstruct_path(current)

        # Mark node 'n' as closed
        open_set.remove(current)
        closed_list.add(current)

        tentative_g = g_score[current] + 1  # Each move cost is 1, adhering to the defined constraints

        # This loop applies the Sucessor Operator to node 'n'
        for d in directions:
            successor = (current[0] + d[0], current[1] + d[1])

            if successor in closed_list:
                continue # Successor already explored

            # Verify if the successor is within bounds and traversable (not an obstacle)
            if 0 <= successor[0] < len(grid) and 0 <= successor[1] < len(grid[0]) and grid[successor[0]][successor[1]] == 1:
                tentative_f = tentative_g + euclid(successor, end)

                if successor not in open_set: # If not explored
                    # Mark successor as open
                    open_list.push((tentative_f, successor))
                    open_set.add(successor)
                elif tentative_g >= g_score[successor]:
                    continue # Successor node not a better path

                # Update the scores for this successor
                predecessors[successor] = current # Record the predecessor
                g_score[successor] = tentative_g
                f_score[successor] = tentative_f

    # Return empty list if no valid path is found (goal unreachable)
    return []
