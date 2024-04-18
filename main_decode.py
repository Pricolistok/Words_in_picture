# Функция добавления длинны в картинку
def find_len(file):
    input_file = open(file, mode='rb')
    header = input_file.read(54)
    res_len = ''
    for byte in input_file.read(16):
        res_len += bin(byte)[-1]
    res_end = input_file.read()
    input_file.close()
    return int(res_len, 2)


def find_message(file, len_message):
    output_file = open(file, mode='rb')
    output_file.read(80)
    bin_message = ''
    for byte in output_file.read(len_message * 8):
        bin_message += bin(byte)[-1]
    elem = ''
    res_arr = []
    print(bin_message)
    for i in range(len(bin_message)):
        elem += bin_message[i]
        if (i + 1) % 8 == 0:
            res_arr.append(elem)
            elem = ''
    ascii_string = ''.join(chr(int(b, 2)) for b in res_arr)
    return ascii_string

def decode(file):
    len_mess = find_len(file)
    return find_message(file, len_mess)
