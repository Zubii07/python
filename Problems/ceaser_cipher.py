import string

def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)  #Shifts each letter forward by the given key value.
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)  #Shifts each letter backward by the given key value.
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_decrypt(cipher_text):
    print("\nBrute-force decryption attempts:")
    for key in range(26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Decrypt a message without key (Brute-force)")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            plain_text = input("Enter the plain text: ")
            key = int(input("Enter the key: "))
            encrypted_text = encrypt(plain_text, key)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            cipher_text = input("Enter the encrypted text: ")
            key = int(input("Enter the key: "))
            decrypted_text = decrypt(cipher_text, key)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            cipher_text = input("Enter the encrypted text: ")
            brute_force_decrypt(cipher_text)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select a valid option.")
