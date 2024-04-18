def input_message():
    input_file = open('input.bmp', mode='rb')
    res_arr = []
    iteration = 0
    flag = 2
    header = input_file.read(54)
    for byte in input_file.read():
        if iteration == 48:
            res_arr.append(255)
            iteration = 0
            flag = 2
        elif flag == 0:
            res_arr.append(byte)
        else:
            res_arr.append(0)
            flag -=1
        iteration += 1
    input_file.close()

    output_file = open('output.bmp', mode='wb+')
    output_file.write(header)
    output_file.write(bytes(res_arr))


def main():
    input_message()


if __name__ == '__main__':
    main()

# ascii_string = ''.join(chr(int(b, 2)) for b in bin_message)
