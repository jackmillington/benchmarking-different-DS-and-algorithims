# Task 1:
import random
import time
import matplotlib.pyplot as plt

# Quick Sort:
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr)/2)] # set pivot as middle element
    l = []
    e = []
    g = []
    for num in arr:
        if num > pivot:
            g.append(num)
        elif num < pivot:
            l.append(num)
        else:
            e.append(num)
    
    leftSorted = quickSort(l)
    rightSorted = quickSort(g)
    return leftSorted + e + rightSorted

# MergeSort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Heapsort
def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Insertion Sort
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort
def selectionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Generate test data
def generate_data(size, data_type):
    if data_type == 'random':
        return [random.randint(0, 10000) for _ in range(size)]
    elif data_type == 'reverse':
        return [i for i in range(size, 0, -1)]
    elif data_type == 'outliers':
        return [random.randint(0, 100) for _ in range(size - 10)] + [10000] * 10
    elif data_type == 'duplicates':
        return [random.randint(0, 100) for _ in range(size)]

# Benchmarking #################################

# Benchmarking sorting algorithms
def benchmark_sorting_algorithms():
    sizes_large = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000]
    sizes_small = [1000, 5000, 10000, 20000]  # Added 20000 as the extra size for testing insertion and selection sort
    data_types = ['random', 'reverse', 'outliers', 'duplicates']
    results = {data_type: [] for data_type in data_types}

    for data_type in data_types:
        for size in sizes_large:
            data = generate_data(size, data_type)
            start_time = time.time()
            quickSort(data.copy())
            quicksort_time = time.time() - start_time
            
            start_time = time.time()
            mergesort(data.copy())
            mergesort_time = time.time() - start_time
            
            start_time = time.time()
            heapsort(data.copy())
            heapsort_time = time.time() - start_time
            
            result = {'size': size, 'quick': quicksort_time, 'merge': mergesort_time, 'heap': heapsort_time}
            
            if size in sizes_small:
                start_time = time.time()
                insertionsort(data.copy())
                result['insertion'] = time.time() - start_time
                
                start_time = time.time()
                selectionsort(data.copy())
                result['selection'] = time.time() - start_time
            
            results[data_type].append(result)
    
    return results

# Visualize results with log scale for x and y axes
def plot_results(results):
    for data_type in results.keys():
        sizes = [result['size'] for result in results[data_type]]
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, [result['quick'] for result in results[data_type]], label='QuickSort', marker='o')
        plt.plot(sizes, [result['merge'] for result in results[data_type]], label='MergeSort', marker='o')
        plt.plot(sizes, [result['heap'] for result in results[data_type]], label='HeapSort', marker='o')
        if 'insertion' in results[data_type][0]:
            plt.plot(sizes[:4], [result['insertion'] for result in results[data_type][:4]], label='InsertionSort', marker='o')
            plt.plot(sizes[:4], [result['selection'] for result in results[data_type][:4]], label='SelectionSort', marker='o')
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('List Size (log scale)')
        plt.ylabel('Time (seconds, log scale)')
        plt.title(f'{data_type.capitalize()} - Sorting Algorithm Performance')
        plt.legend()
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

# Run benchmark test and plot the results
results = benchmark_sorting_algorithms()
plot_results(results)
