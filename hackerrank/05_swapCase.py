def swap_case(s):
    # output = ''
    lower = list('qwertyuiopasdfghjklzxcvbnm')
    upper = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    
    arr = list(s)
    
    for i in range(len(arr)):
        if arr[i] in lower:
            arr[i] = upper[lower.index(arr[i])]
        elif arr[i] in upper:
            arr[i] = lower[upper.index(arr[i])]
        else:
            pass
            
    output = ''.join(arr)
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)