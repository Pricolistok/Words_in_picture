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

    output_file = open('output.bmp', mode='wb+')
    output_file.write(header)
    output_file.write(bytes(res_len))
    output_file.write(res_end)


def main():
    file = 'input.bmp'
    message = 'Hello!'
    input_len(file, message)


if __name__ == '__main__':
    main()
