# Decrypto Tool
# Author: Omar Hisham
# Version: 1.0.0
# Description: A simple tool to decode base16, base32, base64 and Caesar Cipher.
# Usage: python3 Decrypto.py -m MODE -i 'ciphertext'
import sys
import base64

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')',
    '.-..-.': '"', '.----.': "'", '---...': ':', '-.-.-.': ';',
    '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-...': '&', '.--.-.': '@', '...-..-': '$', '.-.-..': '!'
}


def draw_decrypto():
    print("     _                                                       ")
    print("    | |                                                      ")
    print

def draw_decrypto(): 
    print("     _                                                       ")
    print("    | |                                                      ")
    print("  __| | ___   ___ _ __  _   _ ____    __      ____           ")
    print(" / _` |/ _ \ / __| '__/| | | |  _ \ _|__|__ /  __  \         ")
    print("| (_| |  __/| |__| |   | |_| | |_) |_|__|__|  |__|  |        ")
    print(" \__,_|\___| \___|_|    \__, |  __/  |  |   \ ____ /         ")
    print("                         __/ | |     |  |_                   ")
    print("                        |___/|_|      \___|                  ")  




def decode_base16(ciphertext):
    try:
        decoded_bytes = bytes.fromhex(ciphertext)
        plaintext = decoded_bytes.decode("utf-8")
        return plaintext
    except ValueError:
        print("Error: Invalid base 16 input.")
        return None


def decode_base32(ciphertext):
    try:
        decoded_bytes = base64.b32decode(ciphertext)
        plaintext = decoded_bytes.decode("utf-8")
        return plaintext
    except base64.Error:
        print("Error: Invalid base 32 input.")
        return None


def decode_base64(ciphertext):
    try:
        decoded_bytes = base64.b64decode(ciphertext)
        plaintext = decoded_bytes.decode("utf-8")
        return plaintext
    except base64.Error:
        print("Error: Invalid base 64 input.")
        return None

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def decrypt_morse_code(ciphertext):
    words = ciphertext.split(' / ')
    plaintext = ""
    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in MORSE_CODE:
                plaintext += MORSE_CODE[letter]
            else:
                plaintext += '?'
        plaintext += ' '
    return plaintext.strip()


if __name__ == "__main__":
    args = sys.argv
    try:
        # help command
        if len(args) > 1:
            if args[1] == '-h' or args[1] == '--help':
                print("""\n\nUsage:-
        python3 decrypto.py -m MODE -i 'ciphertext'

    Commands:-
        -m, --mode MODE           :- Decoding mode, Check Modes section below
        -i, --input 'ciphertext' :- Encoded ciphertext
        -h, --help               :- Display help
    
    Modes:-
        b16                       :- Base16 Mode
        b32                       :- Base32 Mode
        b64                       :- Base64 Mode
        C                         :- Caesar Cipher
        M                         :- Morse Code
    """)
            # input command
            elif args[1] == "-m" or args[1] == "--mode":
                draw_decrypto()
                if len(args) > 2:
                    mode = args[2]
                    ciphertext = args[4]
                    print("Input mode:", mode)  # Print the selected mode
                    print("Input ciphertext:", ciphertext)  # Print the user input

                    if mode == "b16":
                        decoded_text = decode_base16(ciphertext)
                        if decoded_text:
                            print("Decoded plaintext:", decoded_text)
                    elif mode == "b32":
                        decoded_text = decode_base32(ciphertext)
                        if decoded_text:
                            print("Decoded plaintext:", decoded_text)
                    elif mode == "b64":
                        decoded_text = decode_base64(ciphertext)
                        if decoded_text:
                            print("Decoded plaintext:", decoded_text)
                    elif mode == "C":
                        shift = 3  
                        decrypted_text = decrypt_caesar(ciphertext, shift)
                        if decrypted_text:
                            print("Decrypted plaintext:", decrypted_text)
                    elif mode == "M":
                        decrypted_text = decrypt_morse_code(ciphertext)
                        if decrypted_text:
                            print("Decrypted plaintext:", decrypted_text)
                    else:
                        print("[-] Invalid mode selected.")

                else:
                    print("[-] Incomplete command. Use -h or --help for help.")

            else:
                print("[-] Arguments not recognized. Use -h or --help for help.")

        else:
            print("[-] No arguments passed. Use -h or --help for help.")

    except Exception as e:
        print(f"[-] {e}")
