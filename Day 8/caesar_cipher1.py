alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
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

# def encrypt(text,shift):
#     cipher_text = ''
#     for i in text:
#         position = alphabet.index(i)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"Encrypted code: {cipher_text}") #but here is a problem for letter such as z, limit exceeds, so you need to append alphabets in the alphabet menu


encoded_text = encrypt(text,shift)
print(f"The encoded text is : {encoded_text}")
