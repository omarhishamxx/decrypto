# Decrypto Tool

Author: Omar Hisham

Version: 1.0.0

## Description
Decrypto is a powerful and versatile decoding tool designed to unravel encrypted data encoded in base 16, base 32, and base 64 , caesar, url encoding and morse formats. With Decrypto, you can effortlessly decode and reveal the original content hidden within these popular encoding schemes.
## Features
- Decoding modes:
  - Base16
  - Base32
  - Base64
  - Caesar Cipher
  - Morse Code
  - URL encoding
- Easy-to-use command-line interface
- Supports decoding of multiple encodings in one tool

## Usage
Make sure you have Python 3 installed on your system. To use Decrypto Tool, follow the steps below:

1. Clone this repository or download the `decrypto.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `decrypto.py` file is located.
4. Run the following command to see the available options and modes:
   ```shell
   python3 decrypto.py -h
5.Choose the desired decoding mode using the -m or --mode option, and provide the encoded text using the -i or --input option.
      ```shell
      python3 decrypto.py -m MODE -i 'encoded_text'
6.The tool will output the decoded plaintext, if successful.

## Example
Here's an example of how to use the Decrypto Tool:

- Decode a base64 encoded string:
  ```shell
  python3 decrypto.py -m b64 -i 'SGVsbG8gd29ybGQ='
  
This command will decode the base64 encoded string "SGVsbG8gd29ybGQ=" and display the decoded plaintext "Hello world".

Note: Replace python3 with the appropriate command if you are using a different Python interpreter.
