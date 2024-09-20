Task
A sorted array has been rotated at an unknown pivot point. Given this rotated array and a target value to search for, the objective is to determine the index of the target value in the array. If the target value is not found, the function should return -1.

Explanation
The code uses binary search to find the target element in the rotated array. The search is performed in a while loop that divides the search space in half each time, resulting in a time complexity of O(log n).

The search_rotated_array function uses a binary search algorithm to find the target value in a rotated sorted array. It initializes two pointers, left and right, to the start and end of the array, respectively. It then iteratively divides the array in half and checks if the target value is at the midpoint. If found, it returns the index. If the target is not found after the search, it returns -1.