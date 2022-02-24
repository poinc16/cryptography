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
        decrypt_text = ''
        for i, j in extras.encrypting_lower_alphabet.items():
            if j in text:
                decrypt_text += text.replace(j, i)
        for i, j in extras.encrypting_upper_alphabet.items():
            if j in text:
                decrypt_text += text.replace(j, i)

        for i, j in extras.encrypting_numbers.items():
            if j in text:
                decrypt_text += text.replace(j, i)
        return decrypt_text
    else:
        print('Key inválida.')
        return


def make_file_crypt(text):
    len_keys = len(extras.keys)
    rand_numb = randint(0, len_keys)
    key_to_decrypt = extras.keys[rand_numb]

    with open('######/Encrypted_text.txt', 'w') as file:
        file.write(text + '\n')
        file.write('\n')
        file.write(
            f'# Para descriptografar o texto, utilize a key de dentro dos colchetes: [{key_to_decrypt}].\n')
        file.write(
            '## ATENÇÃO: CASO VOCÊ PERCA ESSA KEY, NÃO SERÁ POSSÍVEL DESCRIPTOGRAFAR O TEXTO.')

    func_return = 'Texto criptografado salvo na pasta "Documentos" do computador.'
    return func_return


def make_file_decrypt(text):
    with open('########/Decrypted_text.txt', 'w') as file:
        file.write(text)

    func_return = 'Texto descriptografado com sucesso! Arquivo salvo na pasta "Documentos" do computador.'

    return func_return
