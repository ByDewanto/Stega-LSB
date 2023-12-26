from PIL import Image

def text_to_binary(text):
    """Converts text to binary."""
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    return binary_message

def encode_message(image_path, message):
    """Encode a binary message into the least significant bit of a grayscale image."""
    # Open the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    
    # Convert the message to binary
    binary_message = text_to_binary(message)

    # Flatten the image pixel values
    pixels = list(img.getdata())

    # Encode the message in the LSB of each pixel
    encoded_pixels = []
    for i in range(len(pixels)):
        pixel_value = pixels[i]
        if pixel_value % 2 == 0 and binary_message:
            # Make the pixel value odd to represent binary '1'
            pixel_value += 1
        elif pixel_value % 2 != 0 and not binary_message:
            # Make the pixel value even to represent binary '0'
            pixel_value -= 1

        encoded_pixels.append(pixel_value)

        # Move to the next bit of the message
        binary_message = binary_message[1:]

    # Create a new image with the encoded pixel values
    encoded_img = Image.new('L', img.size)
    encoded_img.putdata(encoded_pixels)

    # Save the encoded image
    encoded_img.save('encoded_image.png')

def decode_message(encoded_image_path):
    """Decode the hidden message from the least significant bit of a grayscale image."""
    # Open the encoded image
    encoded_img = Image.open(encoded_image_path).convert('L')  # Convert to grayscale

    # Extract the LSB from each pixel and convert to binary
    binary_message = ''.join(str(pixel_value % 2) for pixel_value in encoded_img.getdata())

    # Convert binary to text
    decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    
    return decoded_message

# Example usage
original_image_path = 'D:\steganografi\002\tatoe.png'
message_to_hide = 'D:\steganografi\002\tatoe.txt'

# Encode the message into the image
encode_message(original_image_path, message_to_hide)

# Decode the hidden message from the encoded image
decoded_message = decode_message('encoded_image.png')
print(f'Decoded Message: {decoded_message}')
