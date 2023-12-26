from PIL import Image

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
