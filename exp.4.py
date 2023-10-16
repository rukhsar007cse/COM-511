def linear_search(arr, target):
    """
    Perform linear search to find the target in the list.

    Args:
        arr (list): List of elements.
        target (int): Element to be searched.

    Returns:
        int: Index of the target if found, -1 otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Perform binary search to find the target in the sorted list.

    Args:
        arr (list): Sorted list of elements.
        target (int): Element to be searched.

    Returns:
        int: Index of the target if found, -1 otherwise.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage:

# List of elements (sorted for binary search)
my_list = [2, 4, 7, 10, 13, 17, 22, 25, 29]

# Element to be searched
target_element = 13

# Perform linear search
linear_result = linear_search(my_list, target_element)

# Perform binary search (since the list is sorted)
binary_result = binary_search(my_list, target_element)

# Print the results
print(f"Linear Search Result: {linear_result}")
print(f"Binary Search Result: {binary_result}")
