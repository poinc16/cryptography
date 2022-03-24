from random import randint
import extras


def verify(to_valid):
    try:
        to_valid = int(to_valid)
    except:
        return 'not valid'
    return 'valid'


def main_crypt():
    while True:
        print('Escolha o que você deseja fazer.')
        for i, j in extras.what_to_do.items():
            print(f'[{i}] : {j}')
        choose = input('Digite aqui sua escolha: ')

        valid = verify(choose)

        if valid == 'not valid':
            print('Digite um valor válido!\n')
            continue
        elif valid == 'valid':
            choose = int(choose)
            if choose > 0 and choose < 5:
                if choose == 1:
                    return 'cfile'
                elif choose == 2:
                    return 'dfile'
                elif choose == 3:
                    return 'ctext'
                elif choose == 4:
                    return 'dtext'
            else:
                print('Digite um valor válido!\n')


def read_file_data(file_name):
    with open(file_name, 'r') as file:
        data_file = file.read()
    return data_file


def file_write(data, file_name, type):
    if 'c' in type:
        len_keys = len(extras.keys)
        rand_numb = randint(0, len_keys-1)
        key_to_decrypt = extras.keys[rand_numb]
        with open('Key.txt', 'w') as key_file:
            key_file.write(
                'Utilize esta chave para descriptografar seu arquivo\n\n')
            key_file.write(key_to_decrypt + '\n\n')
            key_file.write(
                '#ATENÇÃO: A perda dessa chave ocasionará na não possibilidade de descriptografia do arquivo.')

    try:
        with open(file_name, 'w') as file:
            file.write(data)
        return 'Operação realizada com sucesso!'
    except BaseException as e:
        with open('log_error.txt', 'w') as error:
            error.write(e)
        return 'Houve um erro ao realizar a operação!'


def data_crypt(text):
    crypt_list = []
    crypt_text = ''

    if len(text) == 1:
        for letter in text:
            for i, c in extras.encrypting_one_bit.items():
                if letter == i:
                    crypt_list.append(c)
    elif len(text) == 2:
        for letter in text:
            for i, c in extras.encrypting_two_bit.items():
                if letter == i:
                    crypt_list.append(c)
    elif len(text) == 3:
        for letter in text:
            for i, c in extras.encrypting_three_bit.items():
                if letter == i:
                    crypt_list.append(c)
    elif len(text) == 4:
        for letter in text:
            for i, c in extras.encrypting_four_bit.items():
                if letter == i:
                    crypt_list.append(c)
    else:
        for letter in text:

            for i, c in extras.encrypting_lower_alphabet.items():
                if letter == i:
                    crypt_list.append(c)

            for i, c in extras.encrypting_numbers.items():
                if letter == i:
                    crypt_list.append(c)

            for i, c in extras.encrypting_upper_alphabet.items():
                if letter == i:
                    crypt_list.append(c)

    for cryp in crypt_list:
        crypt_text += cryp

    return crypt_text


def data_decrypt(text):
    valid = False
    key = input(
        'Insira aqui a key fornecida durante o processo de criptografia: ')
    for k in extras.keys:
        if key == k:
            valid = True

    if valid == True:
        decrypt_text = text
        for i, j in extras.encrypting_lower_alphabet.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_upper_alphabet.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_numbers.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_one_bit.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_two_bit.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_three_bit.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        for i, j in extras.encrypting_three_bit.items():
            if j in text:
                decrypt_text = decrypt_text.replace(j, i)

        return decrypt_text
    else:
        print('Key inválida.')
        return
