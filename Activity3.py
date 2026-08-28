weather = (1,0,0,1,1,0,0)
sunny=0
rainy=0

for i in range(7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1

if sunny > rainy:
    print("\n Good weather\n")
else:
    print("\n Bad weather\n")