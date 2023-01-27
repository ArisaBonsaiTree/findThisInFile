# Simple program to
# https://dotesports.com/tft/news/tft-set-8-cheat-sheet-all-traits-and-stats

exceptions = ["Threat"]
file_one = open("traits.txt", encoding="utf8")
lines = file_one.readlines()
count = 0

for line in lines:
    line = line.replace("\n", "")
    if '(' in line or line in exceptions:
        count += 1
        print(line)

print(count)
