def caesar_cipher_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha(): # Hanya geser karakter alfabet
            start = 65 if char.isupper() else 97
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char # Karakter non-alfabet tidak akan di geser
    return result

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Input message and shift value
message = input("Masukkan pesan: ")
shift_value = int(input("Masukkan nilai shift/pergeseran (1-25): "))

encrypted_message = caesar_cipher_encrypt(message, shift_value)
print("Pesan terenkripsi:", encrypted_message)

decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_value)
print("Pesan terdekripsi:", decrypted_message)
