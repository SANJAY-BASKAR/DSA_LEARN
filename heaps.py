import heapq

# Min heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # Output: 1 (smallest element)
print(heap)                 # Remaining heap: [2, 3]
