# w = write
# a = append

# write a file: 
#with open("examples/march29/test.txt", "w") as file:
    #file.write("Hello World\n")

num = 0
with open("examples/march29/test.txt") as file:
    for line in file:
        num = int(line.strip())
        break

num += 1

with open("examples/march29/test.txt", "w") as file:
    file.write(f"{num}\n")

