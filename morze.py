# morze alphabet
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')
a = '.-'
b ='-...'
c ='-.-.'
d ='-..'
e='.'
f = '..-.'
g = '--.'
h = '....'
i = '..'
j = '.---'
k = '-.-'
l = '.-..'
m = '--'
n = '-.'
o = '---'
p = '.--.'
q = '--.-'
r = '.-.'
s = '...'
t = '-'
u = '..-'
v = '...-'
w = '.--'
x = '-..-'
y = '-.--'
z = '--..'
spc = ' '
mo_alpha = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,spc)
# ask a word

tr = False
# main prg
while not tr:
    str = raw_input('Enter a word to conwert: ')
    str_lo = str.lower() # conwer all letters in lower case

    for i in str_lo:
            if i in alphabet:
                    print mo_alpha[alphabet.index(i)]
            else:
                    print ('you wrote nothing')
    responce = raw_input('\nWould you like to enter anothe sentence? (y/n): ')
    while responce != 'y' and responce != 'n':
        responce = raw_input('\nENTER y or n : ')
    if responce == 'n':
        tr =True

