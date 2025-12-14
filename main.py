import heapq

def min_cost(cables):
    if not cables or len(cables) <= 1:
        return 0

    heapq.heapify(cables)    
    total_cost = 0
    step = 1

    while len(cables) > 1:
        first_smallest = heapq.heappop(cables)
        second_smallest = heapq.heappop(cables)
        current_connection_cost = first_smallest + second_smallest
        total_cost += current_connection_cost
        print(f"Step {step}: join {first_smallest} + {second_smallest}. "
              f"Cost of current connection: {current_connection_cost}. "
              f"\nTotal cost: {total_cost}")
        step += 1
        heapq.heappush(cables, current_connection_cost)
        
    return total_cost

# Usage example
cables = [4, 3, 2, 6, 5, 8, 7, 1, 9, 10]
print("Cables:", cables)
print("Minimal cost:", min_cost(cables)) # 173 (9 steps)