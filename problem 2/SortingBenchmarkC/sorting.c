#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

// Function prototypes
void quickSort(int* arr, int low, int high);
void mergeSort(int* arr, int left, int right);
void heapSort(int* arr, int n);
void insertionSort(int* arr, int n);
void selectionSort(int* arr, int n);
int* generateRandomData(int size);
void benchmarkSortingAlgorithm(void (*sortFunc)(int*, int, int), const char* algoName, int* data, int size);
void benchmarkSortingAlgorithmNoIndices(void (*sortFunc)(int*, int), const char* algoName, int* data, int size);

// QuickSort
void quickSort(int* arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        int pi = i + 1;
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// MergeSort helper function
void merge(int* arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int* L = malloc(n1 * sizeof(int));
    int* R = malloc(n2 * sizeof(int));
    
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
    
    free(L);
    free(R);
}

void mergeSort(int* arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// HeapSort
void heapify(int* arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

// Wrapper for heapSort to match benchmark function signature
void heapSortWrapper(int* arr, int low, int high) {
    heapSort(arr, high + 1);
}

void heapSort(int* arr, int n) {
    for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

// Insertion Sort
void insertionSort(int* arr, int n) {
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
void selectionSort(int* arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
}

// Function to generate random data
int* generateRandomData(int size) {
    int* data = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        data[i] = rand() % 10000; // Random numbers between 0 and 10000
    }
    return data;
}

// Benchmarking function for sorting algorithms
void benchmarkSortingAlgorithm(void (*sortFunc)(int*, int, int), const char* algoName, int* data, int size) {
    struct timeval start, end;
    gettimeofday(&start, NULL);
    
    sortFunc(data, 0, size - 1);
    
    gettimeofday(&end, NULL);
    double duration = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;
    printf("%s took %f seconds.\n", algoName, duration);
}

// Function to benchmark sorting algorithms with no indices (for Insertion and Selection Sort)
void benchmarkSortingAlgorithmNoIndices(void (*sortFunc)(int*, int), const char* algoName, int* data, int size) {
    struct timeval start, end;
    gettimeofday(&start, NULL);
    
    sortFunc(data, size);
    
    gettimeofday(&end, NULL);
    double duration = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;
    printf("%s took %f seconds.\n", algoName, duration);
}

int main() {
    srand(time(0)); // Initialize random seed

    // List of sizes for testing
    int sizes[] = {1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    for (int k = 0; k < num_sizes; k++) {
        int size = sizes[k];
        printf("\nTesting with size: %d\n", size);
        
        // Generate data for each sort to ensure fair comparison
        int* quickSortData = generateRandomData(size);
        int* mergeSortData = generateRandomData(size);
        int* heapSortData = generateRandomData(size);
        int* insertionSortData = generateRandomData(size);
        int* selectionSortData = generateRandomData(size);

        // Benchmark sorting algorithms
        benchmarkSortingAlgorithm(quickSort, "QuickSort", quickSortData, size);
        benchmarkSortingAlgorithm(mergeSort, "MergeSort", mergeSortData, size);
        benchmarkSortingAlgorithm(heapSortWrapper, "HeapSort", heapSortData, size);
        benchmarkSortingAlgorithmNoIndices(insertionSort, "InsertionSort", insertionSortData, size);
        benchmarkSortingAlgorithmNoIndices(selectionSort, "SelectionSort", selectionSortData, size);

        // Free allocated memory
        free(quickSortData);
        free(mergeSortData);
        free(heapSortData);
        free(insertionSortData);
        free(selectionSortData);
    }

    return 0;
}