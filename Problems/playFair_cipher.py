import re

# Function to create 5x5 Playfair key matrix
def create_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Playfair Cipher uses I/J as the same letter
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Fill matrix with key and remaining letters
    matrix = list(key) + [c for c in alphabet if c not in key]
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

# Function to find letter position in matrix
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# Function to prepare plaintext (pairing letters & inserting filler)
def prepare_text(text):
    text = text.upper().replace("J", "I")  # Replace J with I
    text = re.sub(r'[^A-Z]', '', text)  # Remove non-alphabetic characters
    
    prepared_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + "X"  # Add filler if single letter remains
            break
        elif text[i] == text[i + 1]:  # If letters are the same, add filler
            prepared_text += text[i] + "X"
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2
    
    return prepared_text

# Function to encrypt text using Playfair Cipher
def encrypt_playfair(plain_text, matrix):
    prepared_text = prepare_text(plain_text)
    encrypted_text = ""
    
    for i in range(0, len(prepared_text), 2):
        row1, col1 = find_position(matrix, prepared_text[i])
        row2, col2 = find_position(matrix, prepared_text[i + 1])
        
        if row1 == row2:  # Same row: shift right
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column: shift down
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
    
    return encrypted_text

# Function to decrypt text using Playfair Cipher
def decrypt_playfair(cipher_text, matrix):
    decrypted_text = ""
    
    for i in range(0, len(cipher_text), 2):
        row1, col1 = find_position(matrix, cipher_text[i])
        row2, col2 = find_position(matrix, cipher_text[i + 1])
        
        if row1 == row2:  # Same row: shift left
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column: shift up
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]
    
    return decrypted_text

# Main function to run the program
if __name__ == "__main__":
    while True:
        print("\nPlayfair Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            plain_text = input("Enter the plain text: ")
            matrix = create_playfair_matrix(key)
            encrypted_text = encrypt_playfair(plain_text, matrix)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            key = input("Enter the key: ")
            cipher_text = input("Enter the encrypted text: ")
            matrix = create_playfair_matrix(key)
            decrypted_text = decrypt_playfair(cipher_text, matrix)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select a valid option.")
