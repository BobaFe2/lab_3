import re

with open("text.txt","r") as text:
    for line in text:
        line = line.rstrip()
        if re.search(r"z.{3}z", line) is not None:
            print(line)