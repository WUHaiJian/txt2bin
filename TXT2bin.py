
output = []

f = open("test.txt", "rb")
fo = open("out.hex", "wb")

for line in f.readlines():
    # print(line.decode("utf-8"))
    string = line.decode("utf-8")
    data = string.split(",")
    # print(data)

    for i in data:
        if i != '':
            hex = int(i, 16)
            output.append(hex)
            # print("0x%x" % hex)
            data_byte = int(hex).to_bytes(length=1, byteorder='little', signed=False)
            fo.write(data_byte)

# print(output)


