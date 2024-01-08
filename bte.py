from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_file(input_file_path, output_file_path, key):
    with open(input_file_path, 'rb') as file:
        data = file.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    iv = os.urandom(16)
 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

   
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file_path, 'wb') as file:
        file.write(iv + encrypted_data)

key = b'moj_16_bajtowy_k'

encrypt_file('input file path', 'output file path', key)
