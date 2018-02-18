import math
xa = int(input("xa: "))
ya = int(input("ya: "))

yb = int(input("xb: "))
xb = int(input("yb: "))

d = math.sqrt((xb - xa)** 2 + (yb - ya)** 2)

if d >= 10:
    print("longe")
else:
    print("perto")
