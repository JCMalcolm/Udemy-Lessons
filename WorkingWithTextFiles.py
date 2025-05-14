filename = 'source.txt'
# file = open(filename, mode = 'r')
# text = file.read()
# print(text)

# Check to make sure file is open, then close the file
# print(file.closed)
# file.close()
# # Check to make sure file is closed
# print(file.closed)
# # Check to ensure sting still there
# print(text)

# more secure and professional way
with open(filename, mode='r') as out_file:
    text = out_file.read()
print(text)

with open(filename, mode='w') as out_file:
    out_file.write('It is not so simple anymore!')
# writing completely erases the file and puts in what you add

with open(filename, mode='r') as out_file:
    new_text = out_file.read()
print(new_text)





