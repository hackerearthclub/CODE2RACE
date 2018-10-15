# import hashlib module
import hashlib

def hash_file(filename):
   """returns the SHA-1 hash of the file"""

   # hash object
   h = hashlib.sha1()

   # open file and read in binary mode
   with open(filename,'rb') as file:

       # make loop to the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time to save memory
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation
   return h.hexdigest()

message = hash_file("YOUR_FILE.py")
print("SHA-1 key is "+message)
