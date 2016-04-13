fle=raw_input("Enter filename to read: ")
elmnt =[]

rfile = open(fle) # open file
for line in rfile:
    line = line.rstrip() # cut additional \n
    elmnt = elmnt+line.split() # making list from lines
fle2=raw_input("Enter filename to write: ")
rfile = open(fle2,'w') # open file for write
numb=0
for i in elmnt: # for each element in list
    numb+=1
    if '25002' in i:
        j=list(i) # making list from str object
        for iter in range(7,13): # for 7th symb to 13 inc
            j[iter]='*' # replace elmnts of j from 7th ti 13th with asterisk
        i=''.join(j) # assign to i converted in str j with * inside
        rfile.write(i+'\n') # write i in file+ "end line sign"
    elif '~' in elmnt:
        rfile.write(i+'\n')
    else:
        rfile.write(i+'\n')
print "total rows in file: " , numb
rfile.close() # close file

