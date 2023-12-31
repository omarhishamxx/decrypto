# Decrypto Tool
# Author: Omar Hisham
# Version: 1.1
# Description: A simple tool to decode base16, base32, base64 and Caesar Cipher.
# Usage: python3 Decrypto.py -m MODE -i 'ciphertext'
import sys
import base64
import urllib.parse

VERSION = "1.1"
SHIFT_VALUE = 3 

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

def decode_url(ciphertext):
    try:
        decoded_text = urllib.parse.unquote(ciphertext)
        return decoded_text
    except Exception:
        print("Error: Invalid URL-encoded input.")
        return None


if __name__ == "__main__":
    args = sys.argv
    try:
        # help command
        if len(args) > 1:
            if args[1] == '-h' or args[1] == '--help':
                draw_decrypto()
                print("Author: Omar Hisham")
                print("""Usage:-
        python3 decrypto.py -m MODE -i 'ciphertext'

    Commands:-
        -m, --mode MODE               :- Decoding mode, Check Modes section below
        -i, --input 'ciphertext'      :- Encoded ciphertext
        -s, --shift SHIFT_VALUE       :- (Optional) Shift value for Caesar Cipher mode ONLY default is 3
        -h, --help                    :- Display help
        -v, --version                 :- Display version
    
    Modes:-
        b16                           :- Base16 Mode AKA Hexadecimal
        b32                           :- Base32 Mode 
        b64                           :- Base64 Mode
        C                             :- Caesar Cipher
        M                             :- Morse Code
    """)
            elif args[1] == '--version' or args[1] == '-v':
                print("Decrypto Tool, Version", VERSION)
            # input command
            elif args[1] == "-m" or args[1] == "--mode":
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
                        shift_value = SHIFT_VALUE
                        if len(args) >= 6 and (args[5] == "-s" or args[5] == "--shift"):
                            try:
                                shift_value = int(args[6])
                            except ValueError:
                                print("Invalid shift value. Using default value of", SHIFT_VALUE)
                        print("Shift value:", str(shift_value))        
                        decrypted_text = decrypt_caesar(ciphertext, shift_value)
                        if decrypted_text:
                            print("Decrypted plaintext:", decrypted_text)

                    elif mode == "M":
                        decrypted_text = decrypt_morse_code(ciphertext)
                        if decrypted_text:
                            print("Decrypted plaintext:", decrypted_text)
                    elif mode == "U":
                        decoded_text = decode_url(ciphertext)
                        if decoded_text:
                            print("Decoded plaintext:", decoded_text)
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
