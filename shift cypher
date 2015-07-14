# Shifting Code
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')



tr = False
# main prg
while not tr:
    str = raw_input('Enter a word to conwert: ')
    str_lo = str.lower() # conwer all letters in lower case
    key = int(raw_input("Enter a shifting key: "))
    codeco = raw_input("Code or Decode? ")
    string = ""
    for seq in str_lo:
            if seq in alphabet:
                if codeco == "Code":
                    string = string+alphabet[(alphabet.index(seq)+key)%27]
                elif codeco == "Decode":
                    string = string+alphabet[(alphabet.index(seq)-key)%27]
                else:
                    print "wrong action"
            else:
                    print ('you wrote nothing')

    print str_lo
    print string
    responce = raw_input('\nWould you like to enter another sentence? (y/n): ')
    while responce != 'y' and responce != 'n':
        responce = raw_input('\nENTER y or n : ')
    if responce == 'n':
        tr =True
    else:
        string =""
        

