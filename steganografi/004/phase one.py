from PIL import Image
from docx import Document

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

# turning text or word to binary
def read_docx(file_path):
    doc = Document(file_path)
    
    # Initialize an empty string to store the text
    text_content = ""

    # Iterate through paragraphs and add text to the string
    for paragraph in doc.paragraphs:
        text_content += paragraph.text + "\n"

    return text_content

# Example usage
file_path = 'D:/steganografi/example.docx'  # Replace with your Word document path
text_content = read_docx(file_path)

def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

binary_result = text_to_binary(text_content)

binary_text = []

for i in binary_result:
    binary_text.append(int(i))

# slip every bit of it to the last single bit of png binary

# reconstruct it again to the png
def rgb_to_pixel(rgb_values):
    # Flatten the list of RGB tuples into a one-dimensional list of pixel values
    pixels = [value for rgb_tuple in rgb_values for value in rgb_tuple]
    return pixels

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

# Example usage
rgb_values = [
    (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 0)
]  # Replace with your RGB values

width = 2  # Replace with your desired width
height = 2  # Replace with your desired height

pixel_data = rgb_to_pixel(rgb_values)

image = create_image_from_pixel_data(pixel_data, width, height)
image.save('output_image.png')

# recollection
image_path = 'D:/steganografi/003/test.png'
