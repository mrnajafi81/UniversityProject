from modules.password import createRandomPass
from modules.file import getFileContents

fileContents = getFileContents()
fileHeader = fileContents.pop(0)

while True:
    try:
        length = int(input("Enter password length : "))
        break
    except ValueError:
        print('Invalin input, Please enter a number!!')

file = open(f"randomPass_{length}.txt", "w")
file.write(f"{'username':10}\tpassword\n")
for i in range(len(fileContents)):
    file.write(f"{fileContents[i][0]:10}\t{createRandomPass(length)}\n")
file.close()