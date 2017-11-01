fname = input("Enter file name: ")
try :
    fh = open(fname,'r')
except :
    print ("cannot be able to  open the file")
    quit()
for line in fh:
    line = line.strip()
    print (line.upper())
