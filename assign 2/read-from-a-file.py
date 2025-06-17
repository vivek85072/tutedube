file = open("python.txt", "r")  # ('r' = read mode)
content = file.read()
print("File Content:\n", content)
file.close()
