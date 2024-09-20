def sort_012(input_list):
    # Initialize pointers for 0s, 1s, and 2s
    low = 0
    mid = 0
    high = len(input_list) - 1

    # Loop until mid pointer crosses the high pointer
    while mid <= high:
        if input_list[mid] == 0:
            # Swap 0s to the beginning
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            # Move 1s to the middle
            mid += 1
        else:
            # Swap 2s to the end
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

# Test Cases
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# Output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
# Output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([]))
# Output: []

print(sort_012([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# Output: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
