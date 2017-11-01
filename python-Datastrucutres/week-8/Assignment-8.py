"""8.4 Open the file romeo.txt and read it line by line. For each line,
 split the line into a list of words using the split() method.
 The program should build a list of words. For each word on each line check to
 see if the word is already in the list and if not append it to the list.
 When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo
"""
fname = input("Enter file name: ")

try:
    if(len(fname) == 0):
        fname = "mbox-short.txt"
        quit
    else :
        fh = open(fname)
        lst = list()
        for line in fh:
            line =line.strip().split()
            for word in line :
                if word in lst:
                    continue
                else :
                    lst.append(word)

        lst.sort()
        print(lst)
except:
    print("program was errored out due to  the invalid file name or file handler issue")
