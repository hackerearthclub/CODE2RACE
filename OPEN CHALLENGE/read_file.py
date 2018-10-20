file_name = "file1.txt"

file1 = open(file_name,"r")
# replace 0 with the number of line that needs to be extracted.
first_line = file1.readline(0)
# close all the files opened
file1.close()
