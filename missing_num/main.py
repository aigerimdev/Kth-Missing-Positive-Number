def kth_missing_positive_number(arr, k):
    if not arr:
        return k
    start = 0
    end = len(arr)-1
    
    # Binary search to find the point where k missing numbers have occurred
    while start <= end:
        middle = (start + end) // 2
        # Count of missing numbers before arr[middle]
        missing_count = arr[middle] - middle - 1
        if missing_count < k:
            start = middle + 1
        else:
            end = middle - 1
            
    # Calculate how many numbers were missing before index 'start'
    if start == 0:
        return k

    missing_count_before = arr[start - 1] - (start - 1) - 1
    return arr[start - 1] + (k - missing_count_before)

print(kth_missing_positive_number([2,3,4,7,11], 5))
print(kth_missing_positive_number([], 5))
print(kth_missing_positive_number([1,2,3,4], 7))




# def kth_missing_positive_number(numbers, k):
#     '''
#     INPUT: List of positive numbers in increating order & a positive integer k
#     OUTPUT: The kth missing number
#     '''

#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         middle = left + (right - left) // 2
#         missing_nums = numbers[middle] - middle - 1

#         if missing_nums < k:
#             left = middle + 1
#         else:
#             right = middle - 1

#     missing_nums_before = numbers[left - 1] - (left - 1) - 1
#     return numbers[left - 1] + (k - missing_nums_before)