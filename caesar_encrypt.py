"""task1: create a program that can encrypt and decrypt text using the caesar cipher algorithm.Allow users to input 
a message and shift value to perform encryption and decryption"""
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Exiting program...")
            break
            
        if choice in ['1', '2']:
            message = input("Enter the message: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 1 and 25.")
                except ValueError:
                    print("Please enter a valid number.")
            
            if choice == '1':
                result = caesar_encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = caesar_decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
