# Binary Search vs Naive Search Performance Comparison

## Project Description
This Python project demonstrates and compares the performance of two search algorithms:
- Naive Linear Search
- Binary Search

The project implements both algorithms and measures their execution times to prove that binary search is faster than naive search on sorted lists.

## Features
- Implementation of Naive Linear Search algorithm
- Implementation of Binary Search algorithm
- Performance comparison using large datasets
- Random test data generation
- Timing measurements for both algorithms

## Requirements
- Python 3.x
- Required modules:
  - `random` (built-in)
  - `time` (built-in)

## Code Structure
- `main.py`: Contains the implementation of both search algorithms and performance testing code

### Functions
1. `naive_search(lst, target)`
   - Performs linear search through the list
   - Parameters:
     - `lst`: Input sorted list
     - `target`: Element to find
   - Returns: Index of target if found, -1 otherwise

2. `binary_search(lst, target, low=None, high=None)`
   - Performs binary search through the list
   - Parameters:
     - `lst`: Input sorted list
     - `target`: Element to find
     - `low`: Lower bound of search range (optional)
     - `high`: Upper bound of search range (optional)
   - Returns: Index of target if found, -1 otherwise

## Usage
1. Clone the repository
2. Run the script:
```bash
python main.py
```

## Performance Testing
The script includes:
- Test case with small list (commented out)
- Performance comparison with large dataset:
  - List size: 10,000 elements
  - Random integers between -30,000 and 30,000
  - Measures average search time per element

## Sample Output
```
Naive Search Time: 0.00026450555324554443 seconds
Binary Search Time: 4.131460189819336e-06 seconds
```

## Time Complexity
- Naive Search: O(n)
- Binary Search: O(log n)

## Benefits of Binary Search
- Much faster for large datasets
- Logarithmic time complexity
- Efficient for sorted collections

## Limitations
- Binary search requires sorted input
- Additional memory usage for recursive calls
- Not suitable for unsorted lists

