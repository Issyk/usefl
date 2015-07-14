trm = False
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
while not trm:
    pltxt= raw_input("Enter text to encode: ") # plain lst

    kst1 = raw_input("Enter a key: ") # key
    kstr2 ="" # formultiplicated key
    string = ""
    for i in range(0,len(pltxt)):
        kstr2 = kstr2 + kst1[i%len(kst1)] # computing total key for defined txt

    codeco = raw_input("Do you want to 'Code' or 'Decode'? ")
    string = ""
    for seq, i in zip (pltxt,kstr2) : # loop in source and key
        if seq in alphabet:
            if codeco == "Code":
                string = string+alphabet[(alphabet.index(seq)+alphabet.index(i))%27] # coding
            elif codeco == "Decode":
                string = string+alphabet[(alphabet.index(seq)-alphabet.index(i))%27] # decoding 
            else:
                print "wrong action\n"
                continue
        else:
          print ('Alarma!!! Missing symbol\n')

    print "total lenth plain txt is: ", len(pltxt) , '\n'
    print "key string is : " , kst1,'\n'
    print "multiply string is: ", kstr2,'\n'

    print pltxt ,'\n'
    print string,'\n'

    answ = raw_input("Code again? ")
    if answ == 'y':
        kstr2 = ""
        string = ""
        continue
    elif answ =='n':
        trm = True
    else:
        raw_input("again? ")

