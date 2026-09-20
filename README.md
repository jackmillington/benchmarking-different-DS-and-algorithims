# Data Structures & Algorithm Benchmarks

A collection of Python, C, C++ and assembly experiments exploring how different data structures and algorithms behave in practice.

The project focuses on implementation trade-offs, asymptotic complexity and measured performance rather than relying only on theoretical analysis.

## Topics covered

### Queue implementations

Compares queue designs using:

- dynamic arrays
- singly linked lists
- doubly linked lists
- direct node references for constant-time cancellation

The implementations highlight the trade-off between memory overhead and operation complexity.

### Sorting algorithms

Implements and benchmarks:

- QuickSort
- MergeSort
- HeapSort
- Insertion Sort
- Selection Sort
- improved QuickSort variants

Benchmarks exercise multiple input distributions including random, reverse-sorted, duplicate-heavy and outlier-heavy data.

There are also C, C++ and assembly implementations for lower-level performance comparison.

### Ordered storage and search

Implements an ordered warehouse-style collection with:

- sorted insertion
- removal
- binary search
- nearest-value lookup
- operation timing

### Graph pathfinding

Implements Dijkstra-based route selection across a weighted graph, including:

- distance optimisation
- toll optimisation
- weighted distance/toll trade-offs
- filtering of dominated route options

## Repository structure

```text
problem 1/   queue and linked-list implementations
problem 2/   sorting algorithms and benchmarks
problem 3/   ordered storage and binary search
problem 4/   weighted graph pathfinding
```

## Stack

- Python
- C
- C++
- Assembly
- Matplotlib
- algorithm analysis
- benchmarking
- data structures
