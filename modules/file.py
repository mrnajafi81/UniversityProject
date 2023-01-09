def getFileContents():
    file = open("pass.csv", "r")
    fileContents = file.read().split()
    fileContents = list(map(lambda line: line.split(","), fileContents))
    file.close()
    return fileContents
