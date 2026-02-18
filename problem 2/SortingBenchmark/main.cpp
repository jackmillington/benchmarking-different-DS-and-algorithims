#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <algorithm>

// QuickSort
void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        int pi = i + 1;
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// MergeSort
void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// HeapSort
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int>& arr, int low, int high) {
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

// Insertion Sort
void insertionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Selection Sort
void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        std::swap(arr[i], arr[minIdx]);
    }
}

// Function to generate random data
std::vector<int> generateRandomData(int size) {
    std::vector<int> data(size);
    for (int i = 0; i < size; i++) {
        data[i] = rand() % 10000; // Random numbers between 0 and 10000
    }
    return data;
}

// Benchmarking function for sorting algorithms
void benchmarkSortingAlgorithm(void (*sortFunc)(std::vector<int>&, int, int), const std::string& algoName, std::vector<int> data) {

    auto start = std::chrono::high_resolution_clock::now();
    sortFunc(data, 0, data.size() - 1);  // Use the correct function signature

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    
    std::cout << algoName << " took " << duration.count() << " seconds." << std::endl;
}

// Function to benchmark sorting algorithms with no indices (for Insertion and Selection Sort)
void benchmarkSortingAlgorithmNoIndices(void (*sortFunc)(std::vector<int>&), const std::string& algoName, std::vector<int> data) {
    auto start = std::chrono::high_resolution_clock::now();
    sortFunc(data);  // For algorithms that don't need indices
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << algoName << " took " << duration.count() << " seconds." << std::endl;
}

int main() {
    srand(time(0)); // Initialize random seed

    // List of sizes for testing
    std::vector<int> sizes = {1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000};

    for (int size : sizes) {
        std::cout << "\nTesting with size: " << size << "\n";
        std::vector<int> data = generateRandomData(size);

        // Benchmark sorting algorithms
        benchmarkSortingAlgorithm(quickSort, "QuickSort", data);
        benchmarkSortingAlgorithm(mergeSort, "MergeSort", data);
        benchmarkSortingAlgorithm(heapSort, "HeapSort", data);
        benchmarkSortingAlgorithmNoIndices(insertionSort, "InsertionSort", data);
        benchmarkSortingAlgorithmNoIndices(selectionSort, "SelectionSort", data);
    }

    return 0;
}
