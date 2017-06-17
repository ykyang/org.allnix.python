from os import path

sourceFile = 'ex15_example.txt'
targetFile = 'ex17_example.txt'

# print(path.exists(sourceFile))
# print(path.exists(targetFile))

print(f"Copying from {sourceFile} to {targetFile}")

sourceStream = open(sourceFile)
sourceData = sourceStream.read();
sourceStream.close()

print(f"The input file is {len(sourceData)} bytes long")

print(f"Does the output file exist? {path.exists(targetFile)}")
print("Ready, hit ENTER to continue, CTRL-C to abort.")
input()

targetStream = open(targetFile, 'w')
targetStream.write(sourceData)
targetStream.close();
print("Alright, all done.")
