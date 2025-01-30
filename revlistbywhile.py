def rev(n):
    if len(n) < 2:
        return n
    else:
        left = 0
        right = len(n) - 1
        while left <= right:
            n[left], n[right] = n[right], n[left]
            left += 1
            right -= 1
        return n
    
q = [1,2,3,4,5,6,7,8,9]
print(rev(q))
