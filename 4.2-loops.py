for x in range (0,5):
    for y in range (0,10):
        print("#", end = "" )
    print("")

print("")


n=10
for i in range (0,n):
    print(i,"Hello")
    if (i==3):
        print("Count aborted")
        break
    print(i, "World")
print("end")