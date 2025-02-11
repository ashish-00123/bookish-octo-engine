def partition(nums, low, high):
    pivot = nums[low]
    i = low 
    j = high
    while i<j:
        while nums[i] <= pivot and i <= high - 1:
            i+=1
        while nums[j] > pivot and j >= low + 1:
            j-=1
        if i<j:
            nums[i] , nums[j] = nums[j] , nums[i]

    nums[low] , nums[j] = nums[j] , nums[low] 
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind - 1)
        quick_sort(nums, p_ind + 1, high)
    return nums



print(quick_sort([1,9,2,8,3,7,4,6,5], 0, 8))