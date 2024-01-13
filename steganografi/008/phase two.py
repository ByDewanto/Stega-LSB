# Library that used on this program
from PIL import Image
from docx import Document

# Code from PNG to Binary
def rgb_to_binary(rgb):
    return ''.join(format(value, '08b') for value in rgb)

def extracting_image_rgb(img_path):
    image = Image.open(img_path)

    pixel_values = list(image.getdata())

    binary_pixel_values = [rgb_to_binary(rgb) for rgb in pixel_values]

    image.close()
    bit = []
    k = ""
    i = 0

    for three_binary in binary_pixel_values:
        for binary in three_binary:
            i+=1
            k+=binary
            if i == 8 or i == 16 or i == 24:
                bit.append(k)
                k = ""
                i = 0
    return bit

png_file_path = 'D:/steganografi/005/output_image.png'
png_binary = extracting_image_rgb(png_file_path)

count_binary = ""
for i in range(0, 32):
    str_png_binary = png_binary[i]
    count_binary+=(str_png_binary[-1])
print(count_binary)

binary_string = count_binary
count_decimal = int(binary_string, 2)

print(count_decimal)

# Code to get every LSB and put it together
word_binary = ""
for i in range(32, count_decimal+32):
    str_png_binary = png_binary[i]
    word_binary+=(str_png_binary[-1])

def binary_to_text(binary_string):
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    return text

# Example usage
text_result = binary_to_text(word_binary)

print(text_result)

def write_text_to_word(text, output_path='output.docx'):
    # Create a new Word document
    doc = Document()

    # Add the user-input text to the document
    doc.add_paragraph(text)

    # Save the document to the specified path
    doc.save(output_path)

if __name__ == "__main__":
    write_text_to_word(text_result)
    print("Word document created successfully.")