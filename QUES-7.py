def max_sum_k_consecutive(arr, k):
    n = len(arr)
    
    if k > n:
        return "Invalid"
    max_sum = sum(arr[:k])  
    window_sum = max_sum
    
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr1 = [100, 200, 300, 400]
k1 = 2
print("Input:", arr1, "k =", k1)
print("Output:", max_sum_k_consecutive(arr1, k1))  

arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k2 = 4
print("Input:", arr2, "k =", k2)
print("Output:", max_sum_k_consecutive(arr2, k2))  

arr3 = [2, 3]
k3 = 3
print("Input:", arr3, "k =", k3)
print("Output:", max_sum_k_consecutive(arr3, k3))