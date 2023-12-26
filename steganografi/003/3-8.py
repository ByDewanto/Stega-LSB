from docx import Document

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

print(text_content)

def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

binary_result = text_to_binary(text_content)

print(binary_result)

binary_text = []

for i in binary_result:
    binary_text.append(int(i))

print(binary_text)