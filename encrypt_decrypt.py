# File Encryption & Decryption Tool

choice = input("Enter E for Encrypt or D for Decrypt: ")

text = input("Enter your text: ")

result = ""

if choice.upper() == "E":
    for char in text:
        result += chr(ord(char) + 3)
    print("Encrypted Text:", result)

elif choice.upper() == "D":
    for char in text:
        result += chr(ord(char) - 3)
    print("Decrypted Text:", result)

else:
    print("Invalid Choice")
