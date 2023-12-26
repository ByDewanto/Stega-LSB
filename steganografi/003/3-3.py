from PIL import Image

def rgb_to_binary(rgb):
    return ''.join(format(value, '08b') for value in rgb)

# Open an image file
image_path = 'D:/steganografi/003/test.png'
image = Image.open(image_path)

# Get RGB values of each pixel
pixel_values = list(image.getdata())

# Convert RGB values to binary
binary_pixel_values = [rgb_to_binary(rgb) for rgb in pixel_values]

# from left up to right down 

# Display the binary representation of the first few pixels
for i in range(len(pixel_values)):  # Display values for the first 5 pixels
    print(f"{binary_pixel_values[i]}")

# Close the image file
image.close()