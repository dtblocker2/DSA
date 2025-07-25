def count_substring(string, sub_string):
    output = 0
    arr = list(string)
    
    for i in range(len(string)-len(sub_string)+1):
        if arr[i] == sub_string[0]:
            # print(i)
            if ''.join(arr[i:i+len(sub_string)]) == sub_string:
                # print(i)
                output += 1
    return output

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

print(count_substring('ABCDCDC','CDC'))