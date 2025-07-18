if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    # print(records)
    maxNumber = records[0][1]
    for i in range(1, len(records)):
        if records[i][1] < maxNumber:
            maxNumber = records[i][1]

    # Use -infinity so that any valid number will be greater
    secondMin = float('inf')
    for i in range(len(records)):
        if records[i][1] > maxNumber and records[i][1] < secondMin:
            secondMin = records[i][1]

    if secondMin == float('inf'):
        print('No second Min')
    else:
        j = secondMin
    # print(secondMin)
    output = []
    for i in records:
        if i[1] == secondMin:
            output.append(i[0])

    output.sort()

    for i in output:
        print(i)