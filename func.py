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
