from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def decrypt_file(input_file_path, output_file_path, key):
    with open(input_file_path, 'rb') as file:
        iv = file.read(16) 
        encrypted_data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

key = b'moj_16_bajtowy_k' 

input_file = ''
output_file = ''

decrypt_file(input_file, output_file, key)
