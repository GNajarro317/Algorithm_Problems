def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    
    # Perform binary search
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # Check if the target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Check if the target is in the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

# Test Cases
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated_array(nums, target))  # Output: 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(search_rotated_array(nums, target))  # Output: -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
print(search_rotated_array(nums, target))  # Output: 3

nums = [4, 5, 6, 7, 0, 1, 2]
target = 8
print(search_rotated_array(nums, target))  # Output: -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 4
print(search_rotated_array(nums, target))  # Output: 0