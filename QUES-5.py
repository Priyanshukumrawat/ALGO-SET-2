def find_equilibrium_index(arr):
    total_sum = sum(arr) 
    left_sum = 0          

    for i in range(len(arr)):
       
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i + 1  
        left_sum += arr[i]

    return -1 
arr1 = [-7, 1, 5, 2, -4, 3, 0]
print("Input:", arr1)
print("Output:", find_equilibrium_index(arr1))  

arr2 = [1, 2, 3]
print("Input:", arr2)
print("Output:", find_equilibrium_index(arr2)) 

arr3 = [1, 3, 5, 2, 2]
print("Input:", arr3)
print("Output:", find_equilibrium_index(arr3))