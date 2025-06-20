

# Open file in write mode (w)
file = open("python.txt", "w") #This opens a file named python.txt.

# Writing something to the file
file.write("python text file.\n") #This writes the specified string to the file.we can write multiple lines by including \n(newline) characters.
file.write("writing code in python.\n")
file.write("Because file handling is simple and powerful with Python!")

# Close the file
file.close() #this will close the file after writing to ensure the content is properly saved and resources are free now.

print("Content written to python.txt successfully.")

#Output message will confirm the operation is successful.
