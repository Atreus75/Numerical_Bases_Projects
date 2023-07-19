from base_converter import multi_converter


def ascii_binary(ascii):
    ascii = list(ascii)
    binary = ''
    for l in ascii:
        b_octet = multi_converter(ord(l), 'decimal', 'binary')
        b_octet = b_octet[::-1]
        while True:
            if len(b_octet) < 8:
                b_octet += '0'
            else:
                b_octet = b_octet[::-1]
                break
        binary += f' {b_octet}'
    return binary

def binary_ascii(binary):
    binary = list(binary.split(' '))
    ascii = ''.join([chr(int(multi_converter(int(byte), 'binary', 'decimal'))) for byte in binary])
    return ascii

# Usage: ascii_binary('your ascii string')
print(binary_ascii('01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001'))