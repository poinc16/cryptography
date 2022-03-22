from random import randint
import extras


def main_crypt():
    while True:
        print('Escolha o que você deseja fazer.')
        for i, j in extras.what_to_do.items():
            print(f'[{i}] : {j}')
        choose = input('Digite aqui sua escolha: ')
        try:
            choose = int(choose)
        except:
            print('Digite um valor válido!\n')
            continue
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


def file_write(data, file_name):
    with open(file_name, 'w') as file:
        file.write(data)
    return 'Operação realizada com sucesso!'


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
        'Insira aqui a key fornecida durante o processo de criptografia do texto: ')
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


def make_file_crypt(text):
    len_keys = len(extras.keys)
    rand_numb = randint(0, len_keys)
    key_to_decrypt = extras.keys[rand_numb]

    with open('Encrypted_text.txt', 'w') as file:
        file.write(text + '\n')
        file.write('\n')
        file.write(
            f'# Para descriptografar o texto, utilize a key de dentro dos colchetes: [{key_to_decrypt}].\n')
        file.write(
            '## ATENÇÃO: CASO VOCÊ PERCA ESSA KEY, NÃO SERÁ POSSÍVEL DESCRIPTOGRAFAR O TEXTO.')

    func_return = 'Texto criptografado salvo na pasta "Documentos" do computador.'
    return func_return


def make_file_decrypt(text):
    with open('Decrypted_text.txt', 'w') as file:
        file.write(text)

    func_return = 'Texto descriptografado com sucesso! Arquivo salvo na pasta "Documentos" do computador.'

    return func_return
