import heapq

def rearrange_digits(input_list):
    # Create a max heap from the input list
    heap = [-x for x in input_list]
    heapq.heapify(heap)

    # Rearrange the digits into two numbers
    num1 = 0
    num2 = 0
    while heap:
        num1 = num1 * 10 + -heapq.heappop(heap)
        if heap:
            num2 = num2 * 10 + -heapq.heappop(heap)

    return num1, num2

# Test Cases
print(rearrange_digits([1, 2, 3, 4, 5]))
# Output: (531, 42)

print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# Output: (964, 852)

print(rearrange_digits([]))
# Output: (0, 0)

print(rearrange_digits([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
# Output: (99999, 99999)
