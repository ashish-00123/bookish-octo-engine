def palindrome(n):
    l = 0
    r = len(n) - 1 
    while (l >= r):
        if n[l] != n[r]:
            return False
        l += 1
        r -= 1
    return True

a = "cioooouh"
print(palindrome(a))
