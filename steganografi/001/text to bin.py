import os

def text_to_binary(input_file, output_file):
    with open(input_file, 'r') as text_file:
        text_content = text_file.read()

    binary_data = ' '.join(format(ord(char), '08b') for char in text_content)

    with open(output_file, 'wb') as binary_file:
        binary_file.write(bytes([int(i, 2) for i in binary_data.split()]))

# Example usage
input_text_file = "D:\STEGANOGRAFI\Convert TXT to image using Python.txt"
output_binary_file = 'Convert TXT to image using Python.bin'

text_to_binary(input_text_file, output_binary_file)