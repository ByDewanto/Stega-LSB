from PIL import Image

def binary_to_rgb(binary_data):
    # Convert binary data back to RGB values
    rgb_values = [int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)]
    return tuple(rgb_values)

# Example usage
binary_data = "010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101"  # Replace with your binary data
width = 2  # Replace with your desired width
height = 2  # Replace with your desired height

rgbvalues = binary_to_rgb(binary_data)
print(rgbvalues)

from PIL import Image

def create_image_from_rgb(rgb_values, width, height):
    # Create a new image with the specified width and height
    image = Image.new('RGB', (width, height))

    # Create a pixel access object
    pixels = image.load()

    # Iterate through the pixels and set their RGB values
    for y in range(height):
        for x in range(width):
            pixel_index = y * width + x
            pixels[x, y] = rgb_values[pixel_index]

    return image

width = 4  # Replace with your desired width
height = 44  # Replace with your desired height

image = create_image_from_rgb(rgbvalues, width, height)
image.save('output_image.png')

