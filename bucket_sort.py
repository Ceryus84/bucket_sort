"""
Aidan Butcher
CS 3450 - Algorithms & Data Structures
Bucket sort example using the built-in sorted function.
"""


def bucket_sort(arr):
    """Uses the bucket sort algorithm to sort a given array."""
    bucket = []

    # Create empty buckets
    for i in range(10):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


if __name__ == '__main__':
    test_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.99]
    print(f"Original array is: {test_array}")
    print(f"Sorted arry using bucket sort is: {bucket_sort(test_array)}")
