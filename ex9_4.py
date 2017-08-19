name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From:"):continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line, 0) + 1

bigcount = None
bigword = None
for word, sender in counts.items():
    if bigcount == None or sender > bigcount:
        bigword = word
        bigcount = sender

print (bigword, bigcount)
