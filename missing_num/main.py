def kth_missing_positive_number(arr, k):
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
    if start > 0:
        missing_numbers_before = arr[start-1] - (start-1) - 1
        return arr[start-1] + (k - missing_numbers_before)
    else:
        return k