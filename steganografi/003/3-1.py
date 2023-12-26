from PIL import Image

# I apologize for the confusion. It seems I misunderstood your initial request.
# If you want to extract the binary data from the least significant bit (LSB) of each channel separately (R, G, B),
# you need to access each channel using integer indices. Here's the corrected code:

def extract_binary_from_png(image_path, channel_index=0):
    # Open the PNG image
    img = Image.open(image_path)

    # Get the pixel values as a flat list
    pixels = list(img.getdata())

    # Extract the LSB from the specified channel of each pixel and convert to binary
    binary_data = ''.join(str(pixel[channel_index] % 2) for pixel in pixels)

    return binary_data

# Example usage
png_file_path = 'D:/steganografi/003/test.png'

# Extract the LSB from the red channel (index 0)
extracted_binary_data_red = extract_binary_from_png(png_file_path, channel_index=0)
print(f'Extracted Binary Data (Red Channel): {extracted_binary_data_red}')

# Extract the LSB from the green channel (index 1)
extracted_binary_data_green = extract_binary_from_png(png_file_path, channel_index=1)
print(f'Extracted Binary Data (Green Channel): {extracted_binary_data_green}')

# Extract the LSB from the blue channel (index 2)
extracted_binary_data_blue = extract_binary_from_png(png_file_path, channel_index=2)
print(f'Extracted Binary Data (Blue Channel): {extracted_binary_data_blue}')



