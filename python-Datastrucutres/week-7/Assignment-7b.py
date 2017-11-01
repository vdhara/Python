""" Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
## tetxbook - Python for Informatics book

fname = input("Enter file name: ")

try:
    fh = open(fname)
    count = 0
    total = 0
    Average = 0
    if len(fname) == 0 :
     print ('please enter a valid file name')
    else :
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:") : continue
            count = count + 1
            value = float(line[21:])
            total = total + value
    Average = total/count
    print("Average spam confidence:",Average)


except :
    print('File handling exception or invalid file name')
