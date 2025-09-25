lines = []
print("Enter multiple lines of text. Press Enter on an empty line to finish:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

with open("notes.txt", "w", encoding="utf-8") as f:
    for l in lines:
        f.write(l + "\n")

print("\nYour notes have been saved to notes.txt\n")

print("Content of notes.txt:")
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
