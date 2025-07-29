alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,dir):
    cipher_text = ''
    for i in text:
        position = 0
        for j in alphabet:
            position += 1
            if i == j:
                if dir == 'encode':
                    if (shift < len(alphabet)-position):
                        cipher_text += alphabet[position + shift -1]
                    else:
                        overflow =  position + shift - len(alphabet)
                        # print(f"Overflow = {overflow}")
                        cipher_text += alphabet[overflow -1]
                elif dir == 'decode':
                    if (shift < position):
                        cipher_text += alphabet[position - shift -1]
                    else:
                        overflow =  len(alphabet) + position - shift  
                        # print(f"Overflow = {overflow}").
                        cipher_text += alphabet[overflow -1]
                else:
                    print("Invalid.")

    print(f"The {dir}d text is {cipher_text}")
    return cipher_text

caesar(text,shift,dir)