import heapq
from dataclasses import dataclass
from typing import List

# Basic heap operations
print("=== Basic Heap Operations ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(numbers)  # Convert list to heap in-place
print(f"Heapified: {numbers}")

# Add elements
heapq.heappush(numbers, 0)
print(f"After adding 0: {numbers}")

# Remove and return smallest
smallest = heapq.heappop(numbers)
print(f"Removed smallest ({smallest}): {numbers}")

# Peek at smallest without removing
print(f"Smallest element: {numbers[0]}")

print("\n=== Task Scheduling Example ===")
# Priority queue for task scheduling (lower number = higher priority)
tasks = []
heapq.heappush(tasks, (1, "Critical bug fix"))
heapq.heappush(tasks, (3, "Code review"))
heapq.heappush(tasks, (2, "Update documentation"))
heapq.heappush(tasks, (1, "Security patch"))

print("Tasks in priority order:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")

print("\n=== Finding K Largest Elements ===")
data = [1, 23, 12, 9, 30, 2, 50]
k = 3
largest_k = heapq.nlargest(k, data)
smallest_k = heapq.nsmallest(k, data)
print(f"Data: {data}")
print(f"{k} largest: {largest_k}")
print(f"{k} smallest: {smallest_k}")

print("\n=== Custom Objects with Priority ===")
@dataclass
class Patient:
    name: str
    severity: int  # 1=critical, 5=minor
    arrival_time: int
    
    def __lt__(self, other):
        # Primary sort by severity, secondary by arrival time
        if self.severity != other.severity:
            return self.severity < other.severity
        return self.arrival_time < other.arrival_time

# Emergency room priority queue
er_queue = []
patients = [
    Patient("Alice", 3, 1),
    Patient("Bob", 1, 2),    # Critical
    Patient("Carol", 3, 3),
    Patient("Dave", 1, 4),   # Critical
    Patient("Eve", 5, 5)     # Minor
]

for patient in patients:
    heapq.heappush(er_queue, patient)

print("Patients treated in order:")
while er_queue:
    patient = heapq.heappop(er_queue)
    print(f"{patient.name} (severity: {patient.severity}, arrived: {patient.arrival_time})")

print("\n=== Max Heap Implementation ===")
# Python's heapq is min-heap, but we can simulate max-heap by negating values
max_heap = []
values = [3, 1, 4, 1, 5, 9, 2, 6]

# Push negative values for max-heap behavior
for val in values:
    heapq.heappush(max_heap, -val)

print("Max heap (using negated values):")
original_heap = max_heap.copy()
while max_heap:
    # Negate back to get original value
    print(-heapq.heappop(max_heap), end=" ")
print()

print("\n=== Merge K Sorted Lists ===")
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """Efficiently merge multiple sorted lists using a heap."""
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:  # Only add non-empty lists
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_index, element_index)
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from the same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# Example usage
sorted_lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9, 10]
]
merged = merge_k_sorted_lists(sorted_lists)
print(f"Input lists: {sorted_lists}")
print(f"Merged result: {merged}")

print("\n=== Real-world: Dijkstra's Algorithm Skeleton ===")
def dijkstra_example():
    """Skeleton showing how heaps are used in Dijkstra's shortest path algorithm."""
    # Graph represented as adjacency list: {node: [(neighbor, weight), ...]}
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    start = 'A'
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    print(f"Finding shortest paths from {start}:")
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        print(f"Visiting {current_node} with distance {current_dist}")
        
        # Check neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

shortest_paths = dijkstra_example()
print(f"Final distances: {shortest_paths}")