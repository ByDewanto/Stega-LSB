# Library that used on this program
from PIL import Image
from docx import Document

# Code from RGB to Binary
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

def get_png_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None

png_file_path = 'D:/steganografi/testmini.png'
png_binary = extracting_image_rgb(png_file_path)
resolution = get_png_resolution(png_file_path)

length = len(png_binary)

# Code from Word to Binary
def read_docx(file_path):
    doc = Document(file_path)
    
    # Initialize an empty string to store the text
    text_content = ""

    # Iterate through paragraphs and add text to the string
    for paragraph in doc.paragraphs:
        text_content += paragraph.text + "\n"

    return text_content

def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

word_file_path = 'D:/steganografi/example.docx'
word_text = read_docx(word_file_path)
word_binary = text_to_binary(word_text)

# #################################################################

length_count_png_binary = len(png_binary) * 3
length_count_word_binary = len(word_binary) * 8
length_count_word_binary = length_count_word_binary + 32

if length_count_word_binary > length_count_png_binary:
    print("too much")

else:
    dum_list = []
    for i in word_binary:
        dum_list.append(i)
    word_binary = dum_list

    print(len(word_binary))
    dum_list = []
    decimal_number = len(word_binary)
    binary_string = bin(decimal_number)[2:]
    print(binary_string)

    dum_list = []
    j = 0
    for i in range(0, 32):
        if i < (32-len(binary_string)):
            dum_list.append('0')
            continue
        dum_list.append(binary_string[j])
        j = j + 1
    count_word = dum_list

    word_binary = count_word + word_binary

    # Code to slip every binary text to LSB PNG
    new_png_binary = []
    length_png = len(png_binary)
    length_word = len(word_binary)
    for i in range(length_word):
        str_png_binary = png_binary[i]
        new_binary = str_png_binary[:-1] + word_binary[i]
        new_png_binary.append(new_binary)

    for i in range(length_word, length_png):
        new_png_binary.append(png_binary[i])

    #  Code for construct binary png to png
    def create_image_from_pixel_data(pixel_data, width, height):
        # Create a new image with the specified width and height
        image = Image.new('RGB', (width, height))

        # Create a pixel access object
        pixels = image.load()

        # Set pixel values from the pixel data
        for y in range(height):
            for x in range(width):
                pixel_index = y * width * 3 + x * 3
                pixels[x, y] = (pixel_data[pixel_index], pixel_data[pixel_index + 1], pixel_data[pixel_index + 2])

        return image

    rgb_values = []
    dum_list = []

    for i in range(0, len(new_png_binary), 3):
        dum_list = []
        for j in range(3):
            dum_list.append(int(new_png_binary[i+j],2))
        rgb_values.append(dum_list)

    pixel_data = [value for rgb_list in rgb_values for value in rgb_list]

    image = create_image_from_pixel_data(pixel_data, resolution[0], resolution[1])
    image.save('output_image.png')