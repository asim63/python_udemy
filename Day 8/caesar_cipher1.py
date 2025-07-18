alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(input_text,shift):
#     input_text = list(input_text)
#     cipher_text = ''
#     for i in range(0,len(input_text)):
#         for j in range(0,len(alphabet)):
#             if input_text[i]==alphabet[j]:
#                 if(j < len(alphabet)-shift):
#                     input_text[i] = alphabet[j+shift]
#                 else:
#                     overflow = len(alphabet) - shift
#                     input_text[i] = alphabet[overflow]

#     cipher_text = ' '.join(input_text)
#     print(f"Cipher_text: {' '.join(input_text)}")
#     return cipher_text


# def encrypt(text,shift):
#     text = list(text)
#     for i in text:
#         position = 0
#         for j in alphabet:
#             position += 1
#             if i == j:
#                 print(f"i = {i}")
#                 print(f"j = {j}")
#                 if (position < len(alphabet)-shift):
#                     i = alphabet[position + shift]
#                     print(f"After change i = {i} ")
#                 elif(position > len(alphabet) - shift):
#                     overflow = len(alphabet) - shift
#                     i = alphabet[overflow]
#     cipher_text = ''.join(text)
#     print(f"Cipher_text : {cipher_text}")
#     return cipher_text

def encrypt(text,shift):
    cipher_text = ''
    for i in text:
        position = 0
        for j in alphabet:
            position += 1
            if i == j:
                # print(position)
                # print(len(alphabet))
                # print(shift)          #x = pos.24, 5 < 2
                                        #
                if (shift < len(alphabet)-position):
                    cipher_text += alphabet[position + shift -1]
                else:
                    overflow =  position + shift - len(alphabet)
                    # print(f"Overflow = {overflow}")
                    cipher_text += alphabet[overflow -1]
    print(f"Cipher_text : {cipher_text}")
    return cipher_text

encoded_text = encrypt(text,shift)
print(f"The encoded text is : {encoded_text}")
