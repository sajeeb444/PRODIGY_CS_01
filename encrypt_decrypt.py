#Caeser Cipher Encrption & Decryption

def encrypt_decrypt(text, shift, direction):
    result = []
    for char in text:
        if char.isalpha():
            if direction == 'encrypt':
                if char.islower():
                    result.append(chr((ord(char) - 97 + shift) % 26 + 97))
                elif char.isupper():
                    result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            elif direction == 'decrypt':
                if char.islower():
                    result.append(chr((ord(char) - 97 - shift) % 26 + 97))
                elif char.isupper():
                    result.append(chr((ord(char) - 65 - shift) % 26 + 65))
        elif char.isdigit():
            if direction == 'encrypt':
                result.append(str((int(char) + shift) % 10))
            elif direction == 'decrypt':
                result.append(str((int(char) - shift) % 10))
        else:
            result.append(char)
    return result

direction_type = input("Type 'encrypt' or 'decrypt': ")
user_text = input("Type the Message: ")
shift_value = int(input("Enter the shift: "))

result = encrypt_decrypt(user_text, shift_value, direction_type)
print(f"After {direction_type} text: {''.join(result)}")






