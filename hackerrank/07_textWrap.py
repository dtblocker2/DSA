import textwrap

def wrap(string, max_width):
    output = ''
    n = len(string)
    i=0
    while n>0:
        j=i
        i += min(max_width,n)
        output += string[j:i] + '\n'

        n -= max_width

    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)