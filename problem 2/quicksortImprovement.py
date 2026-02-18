import random
import time
import matplotlib.pyplot as plt

# QuickSort Algorithm
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    l, e, g = [], [], []
    for num in arr:
        if num > pivot:
            g.append(num)
        elif num < pivot:
            l.append(num)
        else:
            e.append(num)
    return quickSort(l) + e + quickSort(g)

# Insertion Sort for small subarrays
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, left, right):
    indices = random.sample(range(left, right + 1), 3)
    values = [arr[i] for i in indices]
    values.sort()
    return values[1]

def quick_sort_helper(arr, left, right):
    if right - left < 10:
        insertion_sort(arr, left, right)
        return
    
    pivot = median_of_three(arr, left, right)
    l, e, g = [], [], []
    for num in arr[left:right + 1]:
        if num > pivot:
            g.append(num)
        elif num < pivot:
            l.append(num)
        else:
            e.append(num)
    arr[left:right + 1] = quickSortn(l) + e + quickSortn(g)

def quickSortn(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
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

# Benchmarking sorting algorithms
def benchmark_sorting_algorithms():
    sizes_larger = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000, 1000000, 2000000]
    sizes_small = [1000, 5000, 10000, 20000]
    data_types = ['random', 'reverse', 'outliers', 'duplicates']
    results = {data_type: [] for data_type in data_types}

    for data_type in data_types:
        for size in sizes_larger:
            data = generate_data(size, data_type)
            
            start_time = time.time()
            quickSort(data.copy())
            quicksort_time = time.time() - start_time
            
            start_time = time.time()
            quickSortn(data.copy())
            quicksortn_time = time.time() - start_time
            
            result = {'size': size, 'quick': quicksort_time, 'quickn': quicksortn_time}
            
            if size in sizes_small:
                start_time = time.time()
                insertion_sort(data.copy(), 0, len(data) - 1)
                result['insertion'] = time.time() - start_time
            
            results[data_type].append(result)
    
    return results

# Visualize results
def plot_results(results):
    for data_type in results.keys():
        sizes = [result['size'] for result in results[data_type]]
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, [result['quick'] for result in results[data_type]], label='QuickSort', marker='o')
        plt.plot(sizes, [result['quickn'] for result in results[data_type]], label='QuickSortn', marker='o')
        if 'insertion' in results[data_type][0]:
            plt.plot(sizes[:4], [result['insertion'] for result in results[data_type][:4]], label='InsertionSort', marker='o')
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('List Size (log scale)')
        plt.ylabel('Time (seconds, log scale)')
        plt.title(f'{data_type.capitalize()} - Sorting Algorithm Performance')
        plt.legend()
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

# Run benchmark and plot results
results = benchmark_sorting_algorithms()
plot_results(results)