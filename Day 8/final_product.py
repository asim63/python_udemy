from caesar_arts import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
decision = True
while(decision):
    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    def caesar(text,shift,dir):
        cipher_text = ''
        for i in text:
            if i == ' ' :
                cipher_text += " "
            elif i in numbers:
                cipher_text += i
            else:
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

        print(f"The {dir}d text is {cipher_text}\n")
        return cipher_text

    caesar(text,shift,dir)
    que = input("Do you want to continue the program once again? : (Type Y or N)\n")
    if que == 'Y':
        decision = True
    else:
        decision = False
        print("Goodbye\n")