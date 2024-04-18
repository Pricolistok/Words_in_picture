import os
# Функция добавления длинны в картинку
def input_len(file, message):
    input_file = open(file, mode='rb')
    header = input_file.read(54)
    len_message = len(message)
    len_message_bin = (16 - len(bin(len_message)[2:])) * '0' + bin(len_message)[2:]
    res_len = []
    iteration = 0
    for byte in input_file.read(16):
        res_len.append(int((8 - len(bin(byte)[2:])) * '0' + bin(byte)[2:-1] + len_message_bin[iteration], 2))
        iteration += 1
    res_end = input_file.read()
    input_file.close()

    output_file = open('output_len.bmp', mode='wb+')
    output_file.write(header)
    output_file.write(bytes(res_len))
    output_file.write(res_end)


def input_message(file, message):
    output_file_len = open('output_len.bmp', mode='rb')
    header = output_file_len.read(80)
    print([(8 - len(bin(ord(c))[2:])) * '0' +  bin(ord(c))[2:] for c in message])
    bin_message = ''.join([(8 - len(bin(ord(c))[2:])) * '0' +  bin(ord(c))[2:] for c in message])
    len_bin_mes = len(bin_message)
    res_arr = []
    iteration = 0
    for byte in output_file_len.read(len_bin_mes):
        res_arr.append(int((7 - len(bin(byte)[2:])) * '0' + bin(byte)[2:-1] + bin_message[iteration], 2))
        iteration += 1
    res_end = output_file_len.read()
    output_file_len.close()

    output_file = open(file[:-4] + '_output' + '.bmp', mode='wb+')
    output_file.write(header)
    output_file.write(bytes(res_arr))
    output_file.write(res_end)
    os.remove('output_len.bmp')


def coding(file, message):
    input_len(file, message)
    input_message(file, message)

