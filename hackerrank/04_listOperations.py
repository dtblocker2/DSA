if __name__ == '__main__':
    N = int(input())
    output = []
    for _ in range(N):
        query = input()
        queryList = query.split()
        match queryList[0]:
            case 'append':
                output.append(int(queryList[1]))

            case 'insert':
                output.insert(int(queryList[1]), int(queryList[2]))

            case 'print':
                print(output)

            case 'remove':
                output.remove(int(queryList[1]))

            case 'sort':
                output.sort()

            case 'pop':
                output.pop()
            
            case 'reverse':
                output.reverse()

            

