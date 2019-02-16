def maxDistance(arr, sum):

    curr_sum = arr[0] 
    max_sum = 0
    start = 0 
    for i in range(1,len(arr)):
        if (curr_sum <= sum):
            max_sum = max(max_sum, curr_sum)
        while (((curr_sum + arr[i]) > sum) and start < i): 
            curr_sum -= arr[start] 
            start = start + 1
        curr_sum = curr_sum + arr[i]

    if (curr_sum <= sum):
        max_sum = max(max_sum, curr_sum)

    return max_sum




liste = [3,2,6,12,9,7]
print(maxDistance(liste, 5))