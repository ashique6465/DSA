# def largestSubarr(arr):
#     max_len = 0
#     for i in range(len(arr)):
#         count0 = 0
#         count1 = 0
#         for j in range(i,len(arr)):
#             if arr[j] == 0:
#                 count0 +=1
#             else:
#                 count1 +=1
            
#             if count0 == count1:
#                 max_len = max(max_len,j-i+1)
#     return max_len
# arr= list(map(int,input("Enter the array")))
# print(largestSubarr(arr))
def largest_sub(arr):
    hash_map={}
    max_len = 0
    curr_sum =0
    for i in range(len(arr)):
        if arr[i] == 0:
            curr_sum -=1
        else:
            curr_sum +=1
        if curr_sum == 0:
            max_len = i+ 1
        if curr_sum in hash_map:
            max_len = max(max_len,i- hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
    return max_len
arr = list(map(int, input("Enter the array: ").split()))
print(largest_sub(arr))
