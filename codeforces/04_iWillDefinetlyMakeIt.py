# t = int(input())

# for _ in range(t):
#     pass

output = []

def willReachHighest(heightArr, initialIndex):
    k = initialIndex
    heights = heightArr
    j = initialIndex-1
    initialHeight = heights[initialIndex-1]

    t = 0
    for i in range(len(heights)):
        if heights[i] > initialHeight:
            timeWillTake = heights[i]-initialHeight
            print(timeWillTake)
            if t+timeWillTake <= heights[j]:
                initialHeight = heights[i]
                print(initialHeight)
                t += timeWillTake
                j=i

    maxHeight = max(heightArr)

    # print(maxHeight)

    if maxHeight==initialHeight:
        return 'YES'
    return 'NO'

# print(willReachHighest([1,3,4],1))
print(willReachHighest([3,2,1,4,5],3))

""" wrong answers every damn time """
