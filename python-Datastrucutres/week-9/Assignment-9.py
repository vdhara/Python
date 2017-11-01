name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
name = "mbox-short.txt"
handle = open(name)
text = handle.read()
#words = text.split()

words = list()

for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])


counts = dict()

for word in words:
           counts[word] = counts.get(word, 0) + 1


maximumval = None
maximumkey = None
for key,val in counts.items() :
#   if maxval == None : maxval = val
  if val > maximumval:
      maximumval = val
      maximumkey = key

print (maximumkey, maximumval)
