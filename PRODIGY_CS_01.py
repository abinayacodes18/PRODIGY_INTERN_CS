def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():

            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)

            elif char.islower():
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += new_char
        else:
            result += char

    return result

def main():
    while True:
        print("Caesar Cipher Algorithm")
        mode = input("Do you want to encrypt or decrypt the message? (Type 'encrypt' or 'decrypt'): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please type 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        result = caesar_cipher(message, shift, mode)
        print(f"The resulting message is: {result}")

        another = input("Do you want to process another message? (Type 'yes' or 'no'): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
