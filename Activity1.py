tuplex = ("tuplex", 32.1, 6, False)
print(tuplex)

tuplex = (1,2,333,4,5,6,7,8)
print("Before: ", tuplex)
tuplex = tuplex +(9,70)
print("After:", tuplex)

tuple1 = (50, 20, 66, 50, 66, 30, 40, 50)
print("50s in this tuples:", tuple1.count(50))

tuplex = (8,2,3,5,1,6,7,9,4,10)
_slice = tuplex[5:9]
print(_slice)

_slice = tuplex[:6]
print(_slice)