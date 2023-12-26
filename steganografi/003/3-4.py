from PIL import Image

def rgb_to_binary(rgb):
    return ''.join(format(value, '08b') for value in rgb)

image_path = 'D:/steganografi/003/tatoe.png'
image = Image.open(image_path)

pixel_values = list(image.getdata())

binary_pixel_values = [rgb_to_binary(rgb) for rgb in pixel_values]

# for i in range(len(pixel_values)):
#     print(f"[{i + 1}] {binary_pixel_values[i]}")

# Close the image file
image.close()

listbit = []
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

print(bit)

# def save_list_to_txt(lst, file_path):
#     with open(file_path, 'w') as file:
#         for item in lst:
#             file.write(str(item) + '\n')

# save_list_to_txt(bit, 'output.txt')