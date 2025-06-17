# Open file in write mode (w)
file = open("python.txt", "w")

# Writing something to the file
file.write("python text file.\n")
file.write("writing code in python.\n")
file.write("Because file handling is simple and powerful with Python!")

# Close the file
file.close()

print("Content written to python.txt successfully.")
