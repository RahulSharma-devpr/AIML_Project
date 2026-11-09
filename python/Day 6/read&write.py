with open("notes.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("notes.txt", "a") as f:
    f.write("Line 3\n")

with open("notes.txt", "r") as f:
    for line in f:                 # read line by line (memory friendly)
        print(line.strip())

with open("notes.txt") as f:
    all_text = f.read()            # whole file as one string
    # f.readlines() would give a list of lines

try:
    with open("missing.txt") as f:
        pass
except FileNotFoundError:
    print("File not found")