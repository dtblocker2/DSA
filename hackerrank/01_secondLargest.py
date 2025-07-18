if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    maxNumber = arr[0]
    j = 0
    for i in range(len(arr)):
        if arr[i] > maxNumber:
            maxNumber = arr[i]
            j = i
    secondMax = arr[0]
    for i in range(len(arr)):
        if arr[i] > secondMax and arr[i] < maxNumber:
            secondMax = arr[i]
            j = i
    
    print(secondMax)

""" 
corect answer
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    maxNumber = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxNumber:
            maxNumber = arr[i]

    # Use -infinity so that any valid number will be greater
    secondMax = -float('inf')
    for i in range(len(arr)):
        if arr[i] < maxNumber and arr[i] > secondMax:
            secondMax = arr[i]

    if secondMax == -float('inf'):
        print('No second Max')
    else:
        print(secondMax)
 """