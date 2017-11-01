try :
    text = "X-DSPAM-Confidence:    0.8475";
    pos = text.find('0')
    print float(text[pos:])
except :
    print ("Error throwing at finding the position")
