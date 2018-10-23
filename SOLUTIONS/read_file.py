filename = input("Please type the filename including the format (Ex: filename.txt): ")
file = open(filename, 'r')
c = file.read(1)
fileContent = ''
while (c != '\n'):
    fileContent += c
    c = file.read(1)

print(fileContent) #this is not needed, but hey, whatever