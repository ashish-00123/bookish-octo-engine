def func(list, left , right):
    if left >= right:
        return
    list[left] , list[right] == list[right] , list[left]
    func(list, left + 1 , right - 1)

def arrrev(list, left , right):
    self.func(list , left , right)
    return list

