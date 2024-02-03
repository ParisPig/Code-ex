import time
import random


def timeby(func):
    def wrapper(*args,**kwargs):
        t1 = time.perf_counter()
        func(*args,**kwargs)
        t2 = time.perf_counter()
        print(func.__name__, 'time:', t2 - t1)
    return wrapper

#nums = [23,45,2,344,56,86,4,63,50]
nums = [random.randint(10,1000) for _ in range(10)]

#堆排序
def heapify(nums,n,i):
    current = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[current]:
        current = left
    if right < n and nums[right] > nums[current]:
        current = right
    if current != i:
        nums[current], nums[i] = nums[i], nums[current]
        heapify(nums,n,current)

@timeby
def heap(nums):
    n = len(nums)
    for i in range(n,-1,-1):
        heapify(nums,n,i)
    for i in range(n-1,0,-1):
        nums[0],nums[i] = nums[i], nums[0]
        heapify(nums,i,0)

heap(nums)
print(nums)

#归并排序
def merge(left,right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def mergesort(nums):
    n = len(nums)
    if n == 1:
        return nums
    mid = n // 2
    left = mergesort(nums[0:mid])
    right = mergesort(nums[mid:])
    return merge(left,right)

res = mergesort(nums)
print(res)

#快速排序
def quick(nums,start,end):
    if start >= end: return
    priovt = nums[start]
    low = start
    high = end
    while low < high:
        while low < high and nums[high] > priovt:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < priovt:
            low += 1
        nums[high] = nums[low]
    nums[high] = priovt
    quick(nums,start,low-1)
    quick(nums,low+1,end)
quick(nums,0,len(nums)-1)
print(nums)

#希尔排序
def shell(nums):
    n = len(nums)
    if n <= 1: return nums
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j - gap >= 0 and nums[j - gap] > nums[j]:
                nums[j-gap], nums[j] = nums[j], nums[j - gap]
                j -= gap
        gap = gap // 2
    return nums
print(shell(nums))


#冒泡排序
def Bubble(nums):
    n = len(nums)
    if n <= 1: return nums
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
print(Bubble(nums))


#插入排序
def Insert(nums):
    n = len(nums)
    if n <= 1: return nums
    for i in range(1,n):
        j = i
        res = nums[j]
        while j > 0 and res < nums[j - 1]: #只需要将res与该值相比较即可
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = res
    return nums
print(Insert(nums))


#选择排序
def choice(nums):
    n = len(nums)
    if n <= 1: return nums
    for i in range(n):
        index = i
        for j in range(i,n):
            if nums[index] > nums[j]:
                index = j
        if index != i:
            nums[index], nums[i] = nums[i], nums[index]
    return nums

print(choice(nums))