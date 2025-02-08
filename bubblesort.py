def bubblesort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            return nums
    return nums
print(bubblesort([1, 3, 2, 4, 5, 6, 7, 8, 9]))