import func

initial_choice = func.main_crypt()

if initial_choice == 'cfile':
    file_to_crypt = input(
        'Digite aqui o diretório completo da pasta a ser criptografada: ')

    data_to_crypt = func.read_file_data(file_to_crypt)

    crypted_data = func.data_crypt(data_to_crypt)

    print(func.file_write(crypted_data, file_to_crypt, initial_choice))

elif initial_choice == 'dfile':
    file_to_decrypt = input(
        'Digite aqui o diretório completo da pasta a ser descriptografada: ')

    data_to_decrypt = func.read_file_data(file_to_decrypt)

    decrypted_data = func.data_decrypt(data_to_decrypt)

    print(func.file_write(decrypted_data, file_to_decrypt, initial_choice))

elif initial_choice == 'ctext':
    text_to_crypt = input('Digite o texto a ser criptografado: ')

    crypted_text = func.data_crypt(text_to_crypt)

    print(func.file_write(crypted_text, 'Encrypted_text.txt', initial_choice))

elif initial_choice == 'dtext':
    text_to_decrypt = input('Digite o texto a ser descriptografado: ')

    decrypted_text = func.data_decrypt(text_to_decrypt)

    print(func.file_write(decrypted_text, 'Decrypted_text.txt', initial_choice))
