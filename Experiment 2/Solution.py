import random
import time

# --- Utility: Compare function ---
def compare(ele1, ele2):
    if ele1 < ele2:
        return -1
    elif ele1 == ele2:
        return 0
    else:
        return 1

# --- Selection Sort (O(n^2)) ---
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if compare(arr[j], arr[min_idx]) == -1:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Insertion Sort (O(n^2)) ---
def insertionSort(l1):
    for i in range(1, len(l1)):
        for j in range(i, 0, -1):
            if compare(l1[j], l1[j - 1]) == -1:
                l1[j], l1[j - 1] = l1[j - 1], l1[j]
            else:
                break
    return l1

# --- Merge Sort (O(n log n)) ---
def merge(l1, aux, lo, mid, hi):
    for k in range(lo, hi + 1):
        aux[k] = l1[k]
    
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            l1[k] = aux[j]
            j += 1
        elif j > hi:
            l1[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            l1[k] = aux[i]
            i += 1
        else:
            l1[k] = aux[j]
            j += 1

def mergesort(l1, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    mergesort(l1, aux, lo, mid)
    mergesort(l1, aux, mid + 1, hi)
    merge(l1, aux, lo, mid, hi)

def merge_sort(l1):
    aux = [0] * len(l1)
    mergesort(l1, aux, 0, len(l1) - 1)
    return l1

# --- Quick Sort (O(n log n) average) ---
def quickSort(l1, lo, hi):
    if lo >= hi:
        return l1
    p = partition(l1, lo, hi)
    quickSort(l1, lo, p - 1)
    quickSort(l1, p + 1, hi)
    return l1

def partition(l1, lo, hi):
    i = lo + 1
    j = hi
    v = l1[lo]
    while True:
        while i <= j and l1[i] <= v:
            i += 1
        while i <= j and l1[j] >= v:
            j -= 1
        if i <= j:
            l1[i], l1[j] = l1[j], l1[i]
        else:
            break
    l1[lo], l1[j] = l1[j], l1[lo]
    return j

def quick_sort(l1):
    return quickSort(l1, 0, len(l1) - 1)

# --- Timer function ---
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# --- Generate random data for testing ---
def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# --- Main function to run the experiment ---
def run_experiment():
    # Input sizes to test
    input_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    results = []

    for size in input_sizes:
        arr = generate_random_array(size)
        print(f"Testing input size: {size}")

        # Create copies of the array for each sorting algorithm
        selection_arr = arr.copy()
        insertion_arr = arr.copy()
        merge_arr = arr.copy()
        quick_arr = arr.copy()

        # Run selection and insertion sort only for small sizes
        if size <= 10000:
            selection_time = measure_time(selection_sort, selection_arr)
            insertion_time = measure_time(insertionSort, insertion_arr)
        else:
            selection_time = None
            insertion_time = None

        merge_time = measure_time(merge_sort, merge_arr)
        quick_time = measure_time(quick_sort, quick_arr)

        # Append the results to the table
        results.append({
            "Input Size": size,
            "Selection Sort (s)": selection_time,
            "Insertion Sort (s)": insertion_time,
            "Merge Sort (s)": merge_time,
            "Quick Sort (s)": quick_time,
        })

        # Print the execution times
        if selection_time is not None:
            print(f"Selection Sort: {selection_time:.6f} seconds")
        else:
            print("Selection Sort: N/A")
        if insertion_time is not None:
            print(f"Insertion Sort: {insertion_time:.6f} seconds")
        else:
            print("Insertion Sort: N/A")
        print(f"Merge Sort: {merge_time:.6f} seconds")
        print(f"Quick Sort: {quick_time:.6f} seconds")
        print("-" * 50)
    
    # Output the results table
    print("Experiment Results (in seconds):")
    print("| Input Size | Selection Sort | Insertion Sort | Merge Sort | Quick Sort |")
    print("|------------|----------------|----------------|------------|------------|")
    for result in results:
        selection_str = f"{result['Selection Sort (s)']:.6f}" if result['Selection Sort (s)'] is not None else "N/A"
        insertion_str = f"{result['Insertion Sort (s)']:.6f}" if result['Insertion Sort (s)'] is not None else "N/A"
        print(f"| {result['Input Size']:10} | {selection_str:14} | {insertion_str:14} | {result['Merge Sort (s)']:.6f} | {result['Quick Sort (s)']:.6f} |")

if __name__ == "__main__":
    run_experiment()
