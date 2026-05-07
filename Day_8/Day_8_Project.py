# Caesar Cipher Project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    message_box = ''
    for letter in text:
        if letter in alphabet:
            temp_index = (alphabet.index(letter) + shift) % len(alphabet)
            message_box += alphabet[temp_index]           
        else:
            message_box += letter

    print(message_box)

def decrypt(text, shift):
    message_box = ''
    for letter in text:
        if letter in  alphabet:
            temp_index = (alphabet.index(letter) - shift) % len(alphabet)
            message_box += alphabet[temp_index]
        else:
            message_box += letter

    print(message_box)


caesar_on = True
while caesar_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Enter a valid choice..")
    
    enc_dec_more = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if enc_dec_more == 'no':
        caesar_on = False

