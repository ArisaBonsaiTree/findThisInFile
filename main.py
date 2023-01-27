# Simple program to
# https://dotesports.com/tft/news/tft-set-8-cheat-sheet-all-traits-and-stats

exceptions = ["Threat", "One-cost", "Two-cost", "Three-cost", "Four-cost", "Five-cost"]
file_one = open("traits.txt", encoding="utf8")
lines = file_one.readlines()
count = 0

for line in lines:
    line = line.replace("\n", "")
    if '(' in line or line in exceptions:
        count += 1
        print(line)

print(count)

print("=================")

file_two = open("getchamps.txt", encoding="utf8")
lines = file_two.readlines()


# We want to read a file and get all the champs and get their cost

for line in lines:

    line = line.replace("\n", "")

    list = line.split(" ")

    if any(line.startswith(ex) for ex in exceptions):
        print("=========")
        print(line)

    if(len(list) == 1 and len(list[0]) > 2):
        print(list[0])
        #print(list)
