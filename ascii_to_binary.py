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


# Usage: ascii_binary('your ascii string')