import mmap
import hashlib
import binascii
filename = '38762118.program2.exe'

print "what do you want the new password to be?"
newpass = raw_input()
passhash = hashlib.sha1(str(newpass)).hexdigest()
newFileBytes = []
while len(passhash) > 0:
    newFileBytes.append(int(passhash[:2], 16))
    passhash = passhash[2:]
newFileByteArray = bytearray(newFileBytes)


with open(filename, 'r+b') as f:
    f.seek(0x0001e020+0x6)
    f.write(newFileByteArray)
