bases = {'binary':2, 'octal':8, 'decimal':10, 'hexadecimal':16}

# That function checks if the number is in the selected base
def valid_number(number, from_base):
    for c in range(0, len(number)):
        if int(number[c]) >= from_base:
            return False
    return True

def convert_to_decimal(number, from_base):
    number = convert_hexadecimal_values(str(number), mode=2) if from_base == 16 else number
    number = number[::-1]
    
    if valid_number(number, from_base) == False:
        raise Exception(f'The value {number} contains numbers greater than the selected base: {from_base}')
    p, e, decimal = 0, 0, 0
    while p <= len(number)-1:
        if p == len(number)-1:
            decimal += int(number[p]) * from_base ** e
            p += 1
            e += 1
            continue
        elif from_base == 16:
            is_alphabetic_number = str(number[p] + number[p+1])[::-1] in ['10', '11', '12', '13', '14', '15']
            if is_alphabetic_number:
                alphabetic_number = number[p] + number[p+1]
                decimal += int(alphabetic_number[::-1]) * (from_base ** e)
                p += 2
                e += 1
                continue
        decimal += int(number[p]) * from_base ** e
        p += 1
        e += 1
    return decimal
        

# Main function. This converts the hexadecimal, binary, octal and  decimal bases for each other
def multi_converter(number, from_base, to_base):
    from_base, to_base = bases[from_base], bases[to_base]
    number = str(convert_to_decimal(str(number), from_base))
    # Returns zero if the number received was zero    
    if number == '0':
        return number
    
    # Verify if the number is hexadecimal and had alphabetic characters in it
    number = convert_hexadecimal_values(number, mode=2)
    number = int(number)
    # Divide the number and the results of the operations till zero, and reverse the rests of it
    # See more here: https://byjus.com/maths/number-system-conversion/
    result = ''
    while number != 0:
        result += str(number % to_base)
        number = number // to_base
    if from_base == 16:
        result = convert_hexadecimal_values(result, mode=1)
    return result[::-1]


# This converts alphabetic characters to numeric ones, so the program can perform calculations on them
def convert_hexadecimal_values( number='', mode=1):
    values = [['A', 10], ['B', 11], ['C', 12], ['D', 13], ['E', 14], ['F', 15]]
    # Mode 1 corresponds to: convert numeric characters to alphabetic
    if mode == 1:
        for value in values:
            number = number.replace(str(value[1]), value[0]) if str(value[1]) in number else number
    # Mode 2 corresponds to: convert alphabetic characters to numeric
    elif mode == 2:
        for value in values:
            number = number.replace(value[0], str(value[1])) if value[0] in number.upper() else number
    return number

