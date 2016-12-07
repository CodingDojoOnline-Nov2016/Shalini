def coinflip():
    import random

    flips =0
    heads =0
    tails =0

    while (flips<=5000):
        flipcoin=random.random()
        flips=flips +1

        if(round(flipcoin)==0):
            heads = heads +1
            print "heads"
        elif(round(flipcoin)==1):
            tails =tails +1
            print "tails"
    print "heads:",  heads
    print "tails:",  tails
    print "thanks for playing"
print coinflip()
