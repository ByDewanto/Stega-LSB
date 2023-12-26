import numpy as np
from PIL import Image

def bin_to_image(input_bin_file, output_image_file, width, height):
    with open(input_bin_file, 'rb') as binary_file:
        # Read binary data
        binary_data = binary_file.read()

    # Calculate the expected size based on the specified dimensions and channels
    expected_size = width * height * 3

    # Trim or pad the binary data to match the expected size
    if len(binary_data) < expected_size:
        binary_data += b'\x00' * (expected_size - len(binary_data))
    elif len(binary_data) > expected_size:
        binary_data = binary_data[:expected_size]

    # Convert binary data to a NumPy array of integers
    pixel_values = np.frombuffer(binary_data, dtype=np.uint8)

    # Reshape the array to match the image dimensions
    pixel_values = pixel_values.reshape((height, width, 3))

    # Create an image from the NumPy array
    image = Image.fromarray(pixel_values)

    # Save the image to a file
    image.save(output_image_file)

# Example usage
input_bin_file = 'D:\steganografi\Convert TXT to image using Python.bin'
output_image_file = 'output.png'
image_width = 256
image_height = 256

bin_to_image(input_bin_file, output_image_file, image_width, image_height)
