t = int(input())

output=[]
for _ in range(t):
    n,k = map(int, list(input().split()))
    arr = input().split()
    noOfDaysPossible = 0
    i=0
    counter = 0
    # print(arr)

    while i < len(arr):
        if arr[i]=='0':
            counter += 1
        elif arr[i]=='1':
            counter=0
        if counter == k:
            noOfDaysPossible+=1
            # print(noOfDaysPossible)
            counter = 0
            i+=1
        i+=1

    output.append(noOfDaysPossible)

for i in output:
    print(i)
