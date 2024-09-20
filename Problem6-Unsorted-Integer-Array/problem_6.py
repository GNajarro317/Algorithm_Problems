def get_min_max(ints):
    # Check if the input list is empty
    if not ints:
        return (None, None)

    # Initialize minimum and maximum values 
    min_val = float('inf')
    max_val = float('-inf')

    # Iterate through the list to find min and max values
    for num in ints:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # Return the min and max values 
    return (min_val, max_val)

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 1: Empty List
print("Pass" if ((None, None) == get_min_max([])) else "Fail")

# Test Case 2: Single Element List
print("Pass" if ((5, 5) == get_min_max([5])) else "Fail")

# Test Case 3: List with Negative Numbers
print("Pass" if ((-10, 20) == get_min_max([-10, 5, 20, -5])) else "Fail")

# Test Case 4: List with Extremely Large Numbers
print("Pass" if ((1, 1000000000000000000) == get_min_max([1, 1000000000000000000])) else "Fail")

# Test Case 5: List with Duplicate Elements
print("Pass" if ((1, 5) == get_min_max([1, 3, 5, 5, 3])) else "Fail")