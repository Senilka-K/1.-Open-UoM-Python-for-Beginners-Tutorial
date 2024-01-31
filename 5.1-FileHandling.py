fhandle = open("file1.txt")
lines = fhandle.readlines()[:2]

fhandle = open("file2.txt", "w")
fhandle.writelines(lines)
fhandle.close
fhandle = open("file2.txt", "r")
fcontents = fhandle.read()
print(fcontents)