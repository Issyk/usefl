import itertools, md5
lstelmt,hexdigst,hashlist=[],[],[]
Hashes=open('hashes.txt')# open file with hashes to compare
for line in Hashes:
    hashlist = hashlist+line.rstrip().split() # making list from lines

for i in list(itertools.product('1234567890',repeat=6)):
    lstelmt.append(''.join(i)) #making correct list from numbers secuences

for i in lstelmt:
    mdhash=md5.new() # create md5hash object
    mdhash.update(i)# write number to object
    if mdhash.hexdigest() in hashlist:
        print "password: %s have hash: %s" %(i, mdhash.hexdigest())
