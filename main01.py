from modules.password import decryptPass,isInvalidPass
from modules.file import getFileContents

fileContents = getFileContents()

for l in fileContents:
    if len(l[1]) != 40:
        continue
    decrypt_pass = decryptPass(l[1])
    message = f"username: {l[0]}, password: <<{decrypt_pass}>>"
    if not isInvalidPass(decrypt_pass):
        message+='invalid password'
    print(message)
