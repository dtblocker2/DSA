def get_char_map():
    # Map numbers to their corresponding letters
    return {str(i): chr(64 + i) for i in range(1, 27)}

def decode_string(number, index=0, current_string="", result=None):
    if result is None:
        result = []
    
    # Base case: If the entire number has been processed, add the current string to results
    if index == len(number):
        result.append(current_string)
        return result
    
    # Get the character map
    char_map = get_char_map()
    
    # Process single digit
    if number[index] in char_map:
        decode_string(number, index + 1, current_string + char_map[number[index]], result)
    
    # Process two digits if possible
    if index + 1 < len(number) and number[index:index + 2] in char_map:
        decode_string(number, index + 2, current_string + char_map[number[index:index + 2]], result)
    
    return result

# Input number as string
input_number = "32823"

# Generate all possible strings
output_strings = decode_string(input_number)
print("\n".join(output_strings))
