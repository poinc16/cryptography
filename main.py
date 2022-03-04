import func

initial_choice = func.main_crypt()

if initial_choice == 'cfile':
    pass

elif initial_choice == 'dfile':
    pass

elif initial_choice == 'ctext':
    text_to_crypt = input('Digite o texto a ser criptografado: ')
    crypted_text = func.text_crypt(text_to_crypt)
    print(func.make_file_crypt(crypted_text))

elif initial_choice == 'dtext':
    text_to_decrypt = input('Digite o texto a ser descriptografado: ')
    decrypted_text = func.text_decrypt(text_to_decrypt)
    print(func.make_file_decrypt(decrypted_text))
