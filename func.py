from random import randint
import extras
import os


def main_crypt(to_crypt):
    pass


def file_crypt():
    pass


def text_crypt(text):
    crypt_list = []
    crypt_text = ''

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


def text_decrypt(text):
    valid = False
    key = input(
        'Insira aqui a key fornecida durante o processo de criptografia do texto: ')
    for k in extras.keys:
        if key == k:
            valid = True
    if valid == True:
        pass
    else:
        print('Key inválida.')
        return


def make_file_crypt(text):
    len_keys = len(extras.keys)
    rand_numb = randint(0, len_keys)
    key_to_decrypt = extras.keys[rand_numb]

    with open('/home/matheus/Documentos/Encrypted_text.txt', 'w') as file:
        file.write(text + '\n')
        file.write('\n')
        file.write(
            f'# Para descriptografar o texto, favor inserir a key(sem os colchetes): [{key_to_decrypt}] no local onde for pedido.\n')
        file.write(
            '## ATENÇÃO: CASO VOCÊ PERCA ESSA KEY, NÃO SERÁ POSSÍVEL DESCRIPTOGRAFAR O TEXTO.')

    func_return = 'Texto criptografado salvo na pasta "Documentos" do computador.'
    return func_return


def make_file_decrypt(text):
    pass
