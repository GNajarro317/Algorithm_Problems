def sqrt(n):
    # Base Case, if integer is negative it will stop the recursion since the square root of a negative is not a real number.
    if n < 0:
        return None
    
    left = 0
    right = n

   # Within the loop, it calculates the mid point as the average of left and right. 
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        # If the square of mid is not equal to n the loop will either have to add or subtract one to find the floor value.
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

# Test Cases
print(sqrt(16))
# Output: 4

print(sqrt(27))
# Output: 5

print(sqrt(0))
# Output: 0

print(sqrt(-5))
# Output: None

print(sqrt(222 * 63 - 1))
# Output: 118