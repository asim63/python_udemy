alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text = ''
    for i in text:
        position = 0
        for j in alphabet:
            position += 1
            if i == j:
                if (shift < len(alphabet)-position):
                    cipher_text += alphabet[position + shift -1]
                else:
                    overflow =  position + shift - len(alphabet)
                    # print(f"Overflow = {overflow}")
                    cipher_text += alphabet[overflow -1]
    print(f"Cipher_text : {cipher_text}")
    return cipher_text

def decrypt(text,shift):
    cipher_text = ''
    for i in text:
        position = 0
        for j in alphabet: 
            position += 1
            if i == j:
                if (shift < position):
                    cipher_text += alphabet[position - shift -1]
                else:
                    overflow =  len(alphabet) + position - shift  
                    # print(f"Overflow = {overflow}")
                    cipher_text += alphabet[overflow -1]
    print(f"Cipher_text : {cipher_text}")
    return cipher_text

if dir == 'encode':
    encoded_text = encrypt(text,shift)
    print(f"The encoded text is : {encoded_text}")
elif dir == 'decode':
    decoded_text = decrypt(text,shift)
    print(f"The decoded text is: {decoded_text}")
else:
    print("")
