# **Binary Search Algorithm**
A binary search algorithm is an efficient way to find a specific value in a sorted list or array by repeatedly dividing the search range in half. It works on the principle of "divide and conquer" and has a time complexity of O(log n), making it much faster than a linear search for large datasets.

Here's how binary search works in Python, along with an example implementation:

## **Key Concepts:**

1. **Sorted List:** Binary search requires the input list to be sorted beforehand.
2. **Midpoint:** It compares the target value with the middle element of the current range.
3. **Divide:** If the target is less than the midpoint, it searches the left half; if greater, it searches the right half.
4. **Repeat:** This process continues until the value is found or determined to not exist in the list.

## **Python Implementation:**

Here are two common ways to implement binary search in Python:

### 1. **Iterative Approach:**

``` python

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        
        # If target is found at mid, return the index
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Target not found
    return -1

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 10
result = binary_search_iterative(arr, target)
print(f"Element {target} is at index {result}")  # Output: Element 10 is at index 3

```
### 2. **Recursive Approach:**

``` python

def binary_search_recursive(arr, target, left, right):
    # Base case: if left > right, element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # If target is found at mid, return the index
    if arr[mid] == target:
        return mid
    
    # If target is smaller, search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # If target is greater, search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Example usage
arr = [2, 3, 4, 10, 40, 50, 60, 70]
target = 40
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element {target} is at index {result}")  # Output: Element 40 is at index 4

```

## **Notes:**

* **Precondition:** The array/list must be sorted. If it’s not sorted, you’d need to sort it first using something like arr.sort() (which adds O(n log n) time).

* **Return Value:** Typically, binary search returns the index of the target element if found, or -1 if not found.

* **Efficiency:** O(log n) time complexity because the search space halves with each step.

* **Edge Cases:** Handle empty arrays or cases where the target isn’t in the list.

Binary search is widely used in Python when working with sorted datasets, such as in searching problems, finding boundaries, or optimizing lookups. Let me know if you'd like a deeper dive or more examples!