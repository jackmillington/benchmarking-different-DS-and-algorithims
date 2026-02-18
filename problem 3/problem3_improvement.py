class Warehouse:

    def __init__(self):
        self.items = []

    def shift_elems(self, i): # Shifts the array to insert a new element
        self.items.append(0) # extends the array
        for j in range(len(self.items) - 1, i, -1): # shifts the 0 to where the weight is to be inserted then inserts the weight
            self.items[j] = self.items[j-1]

    def add_item(self, weight):
        # binary search to find where element goes, 
        # denoted by mid, if no mid, then it is inserted into low
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid] == weight:
                self.shift_elems(mid) # shifts array
                self.items[mid] = weight # insert elem
                return
            elif self.items[mid] < weight:
                low = mid + 1
            else:
                high = mid - 1

        # Add new item into low position.        
        self.shift_elems(low)  
        self.items[low] = weight
        return

    def remove_item(self, weight):
        if not self.items:
            return None

        # binary search
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid] == weight:
                for j in range(mid, len(self.items) - 1): # shifts item to end of array
                    self.items[j] = self.items[j+1] 
                self.items.pop() # removes the end element of the array
                return
            elif self.items[mid] < weight:
                low = mid + 1
            else:
                high = mid - 1
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
        
def run_tests():
    w = Warehouse()

    print("\n--- Test 1: Add Items in Random Order ---")
    w.add_item(20)
    w.add_item(5)
    w.add_item(33)
    w.add_item(12)
    w.display_items()  # Expected: [5, 12, 20, 33]

    print("\n--- Test 2: Remove Existing Item ---")
    w.remove_item(12)
    w.display_items()  # Expected: [5, 20, 33]

    print("\n--- Test 3: Remove Non-Existing Item ---")
    w.remove_item(100)  # Expected: "Item not found."
    w.display_items()   # Expected: [5, 20, 33]

    print("\n--- Test 4: Find Exact Match ---")
    result = w.find_item(20)
    print("Find 20 →", result)  # Expected: 20

    print("\n--- Test 5: Find Closest (Lower Bound) ---")
    result = w.find_item(17)
    print("Find 17 →", result)  # Expected: 20 (closer to 20 than 5)

    print("\n--- Test 6: Find Closest (Upper Bound) ---")
    result = w.find_item(30)
    print("Find 30 →", result)  # Expected: 33

    print("\n--- Test 7: Find Closest Below All ---")
    result = w.find_item(1)
    print("Find 1 →", result)  # Expected: 5

    print("\n--- Test 8: Find Closest Above All ---")
    result = w.find_item(100)
    print("Find 100 →", result)  # Expected: 33

    print("\n--- Test 9: Empty List Find ---")
    empty = Warehouse()
    result = empty.find_item(10)
    print("Find 10 in empty list →", result)  # Expected: None

    print("\n--- Test 10: Remove from Empty ---")
    empty.remove_item(10)  # Expected: "Item not found."

run_tests()


