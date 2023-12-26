x = "011100101001000101011100"
j = 0
listbit = []
nya = []
for i in x:
    j = j + 1
    nya.append(int(i))
    if j%8 == 0:
        listbit.append(nya)
        nya = []

# print(j)
# print(listbit)
k = ""

for i in listbit:
    for j in i:
        k = k + str(j)
    print(k)
    k = ""