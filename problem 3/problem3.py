class Warehouse:

    def __init__(self):
        self.items = []

    def add_item(self, weight):
        i = 0
        while i < len(self.items) and self.items[i] < weight: # find position the element goes
            i += 1
        
        self.items.append(0) # extends the array
        for j in range(len(self.items) - 1, i, -1): 
        # shifts the 0 to where the weight is to be inserted then inserts the weight
            self.items[j] = self.items[j-1]
        self.items[i] = weight

    def remove_item(self, weight):
        for i in range(len(self.items)):
            if self.items[i] == weight: # find item to remove
                for j in range(i, len(self.items) - 1): # shifts item to end of array
                    self.items[j] = self.items[j+1] 
                self.items.pop() # removes the end element of the array
                return
        print("item not found")

    def find_item(self, weight) :
        if not self.items:
            return None

        # binary search
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid] == weight:
                return weight
            elif self.items[mid] < weight:
                low = mid + 1
            else:
                high = mid - 1

        # Return closest found element
        if low == 0:
            return self.items[0]
        if low >= len(self.items):
            return self.items[-1]
        
        before = self.items[low - 1] # before final interation
        after = self.items[low] # after final iteration

        if abs(before - weight) <= abs(after - weight):
            return before
        else:
            return after
        
    def display_items(self):
        print(self.items)
        

import time
import random

# === Assumes your AVL-based Warehouse class is already defined above ===

def benchmark_operations(N):
    # Generate N unique elements and shuffle
    data = list(range(N))
    random.shuffle(data)

    # Preload the warehouse with N items
    wh = Warehouse()
    for x in data:
        wh.add_item(x)

    # 1) Benchmark add_item N times (adding new keys N..2N-1)
    add_keys = [x + N for x in data]
    start = time.perf_counter()
    for key in add_keys:
        wh.add_item(key)
    total_add = time.perf_counter() - start

    # 2) Benchmark find_item N times on random keys in [0..2N-1]
    start = time.perf_counter()
    for _ in range(N):
        key = random.randint(0, 2*N - 1)
        wh.find_item(key)
    total_find = time.perf_counter() - start

    # 3) Benchmark remove_item N times (removing the keys we just added)
    start = time.perf_counter()
    for key in add_keys:
        wh.remove_item(key)
    total_remove = time.perf_counter() - start

    print(f"Performed {N} operations each:")
    print(f"  add_item:    {total_add:.6f} seconds total")
    print(f"  find_item:   {total_find:.6f} seconds total")
    print(f"  remove_item: {total_remove:.6f} seconds total")

if __name__ == "__main__":
    N = 10_000
    benchmark_operations(N)
