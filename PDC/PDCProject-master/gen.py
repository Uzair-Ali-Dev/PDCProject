file = open("dummy.txt", "w")
for i in range(0, 100000):
    file.write("name" + str(i) + "\t" + str(i) + "\n")
file.close()
