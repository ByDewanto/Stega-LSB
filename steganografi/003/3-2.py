from PIL import Image

# Open an image file
image_path = 'D:/steganografi/003/test.png'
image = Image.open(image_path)

# Get RGB values of each pixel
pixel_values = list(image.getdata())

# Display the RGB values of the first few pixels
for i in range(5):  # Display values for the first 5 pixels
    print(f"Pixel {i + 1}: {pixel_values[i]}")

# Close the image file
image.close()

# Access RGB values of the first pixel
first_pixel_rgb = pixel_values[0]
red_value = first_pixel_rgb[0]
green_value = first_pixel_rgb[1]
blue_value = first_pixel_rgb[2]

print(f"Red: {red_value}, Green: {green_value}, Blue: {blue_value}")
