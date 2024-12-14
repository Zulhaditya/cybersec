from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)  # Write the initialization vector
        f.write(encrypted_data)

def aes_decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # The first 16 bytes are the initialization vector
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Generate a random key
key = get_random_bytes(16)  # 128-bit key for AES

# Example usage for file encryption
input_filename = input("Masukkan nama file untuk dienkripsi: ")
output_filename = input("Masukkan nama file output terenkripsi: ")

aes_encrypt_file(input_filename, output_filename, key)
print(f"File terenkripsi disimpan sebagai {output_filename}")

# Example usage for file decryption
encrypted_file = input("Masukkan nama file terenkripsi untuk didekripsi: ")
decrypted_filename = input("Masukkan nama file output terdekripsi: ")

aes_decrypt_file(encrypted_file, decrypted_filename, key)
print(f"File terdekripsi disimpan sebagai {decrypted_filename}")
