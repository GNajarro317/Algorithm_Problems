Task
Given an input array that consists solely of the integers 0, 1, and 2, the objective is to sort the array in a single traversal. The solution must not use any built-in sorting functions provided by Python.The sorting must be accomplished in a single pass through the array.

Explanation
The code uses a single pass through the input list with a while loop. In each iteration of the loop, the algorithm performs constant time operations. Therefore, the overall time complexity is O(n), where n is the length of the input list.

Initialize three pointers: low, mid, and high to keep track of the positions of 0s, 1s, and 2s respectively. It iterate through the list using the mid pointer until it reaches the high pointer. Continue this process ensuring all 0s are on the left, 1s in the middle, and 2s on the right of the list.