# celsius to fahrenheit


# def printTable(start, end, step):
#     currentValue = start
#     while(currentValue <= end):
#         fValue = int((5/9)*(currentValue-32))
#         print(currentValue, end="\t")
#         print(fValue)
#         currentValue = currentValue + step


# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s, e, step)


# Array Sum
# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# result = 0
# for i in arr:
#     result += i
# print(result)

# find the Difference

# def difference(arr):
#     n = len(arr)
#     even = 0
#     odd = 0
#     for j in range(0, n, 2):
#         even += arr[j]
#     for j in range(1, n, 2):
#         odd += arr[j]
#     return even-odd


# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# diff = difference(arr)
# print(diff)


# LINEAR SEARCH

# def linear(arr, val):
#     n = len(arr)
#     for j in range(0, n):
#         if(val == arr[j]):
#             return j
#     return -1


# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# val = int(input())
# index = linear(arr, val)
# print(index)


# SWAP ALTERNATE

# def swap(arr):
#     size = len(arr)
#     for j in range(0, size-1, 2):
#         number = arr[j]
#         arr[j] = arr[j+1]
#         arr[j+1] = number


# n = int(input())
# arr = list(int(i) for i in input().strip().split(' '))
# swap(arr)
# for i in arr:
#     print(i, end=' ')
# print()


# FIND UNIQUE

def unique(arr):
    size = len(arr)
    for i in range(0, size):
        for j in range(0, size):
            if(arr[i] == arr[j] and i != j):
                break
            else:
                return arr[i]


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
number = unique(arr)
print(number)
