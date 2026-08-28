def palind(tuple):
    e = len(tuple)-1
    s = 0
    while s<e:
        if(tuple[s] != tuple[e]):
            return False
        s+=1
        e-=1
    return True

tuple = (1,2,3,2,1)

if(palind(tuple)):
    print("This tuple is a Flip-Flop")
else:
    print("This tuple is not a Flip-Flop")
