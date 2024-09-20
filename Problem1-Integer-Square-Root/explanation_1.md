Task
The task is to find the square root of a given integer without using any Python libraries, specifically returning the floor value of the square root. 

Explanation
The time complexity of this code is O(log n). The code uses binary search to find the square root of a number. The search space is reduced by half in each iteration, resulting in a logarithmic time complexity.

The sqrt function takes an integer n as input and calculates its square root using a binary search approach. Where it initializes left to 0 and right to n, setting up the search range. It enters a while loop that continues until left exceeds right. If the square of mid equals n, it returns mid as the square root. If the square of mid is less than n, it updates left to mid + 1 to search in the right half. If the square of mid is greater than n, it updates right to mid - 1 to search in the left half. It returns the value of right, the floor of the square root of n.