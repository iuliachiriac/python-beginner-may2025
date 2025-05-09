with open("functions.py") as f:
    for line in f:
        if "def" in line:
            print(line.strip())


with open("out.txt", "w") as f:
    f.write("hello\n")
    f.write("world")
    f.write("test")
