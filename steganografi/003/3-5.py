def read_txt_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Example usage
file_path = 'D:/steganografi/output.txt'
file_lines = read_txt_file_line_by_line(file_path)

i = 0
list_binary = []
list_3binary = []


# Print each line
for line in file_lines:
    list_binary.append(line.strip())  # strip() removes the newline characters at the end of each line
    i = i + 1
    if i%3== 0 and i != 0:
        list_3binary.append(list_binary)
        i = 0
        list_binary = []

j = ''
k = 0
blyat = []

for onebinary in list_3binary:
    for i in onebinary:
        j = j + i
        k = k + 1
        if k%3 == 0 and k != 0:
            blyat.append(j)
            j = ''
            k = 0

print(blyat)