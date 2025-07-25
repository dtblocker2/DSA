import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        # Create the sequence: e-d-c-... up to current letter and back
        left = alphabet[size-1:i:-1]
        center = alphabet[i]
        right = alphabet[i+1:size]
        row_letters = list(left) + [center] + list(right)
        row = '-'.join(row_letters)
        lines.append(row.center(4 * size - 3, '-'))

    # Combine top and bottom parts
    full_rangoli = lines[::-1] + lines[1:]
    print('\n'.join(full_rangoli))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)