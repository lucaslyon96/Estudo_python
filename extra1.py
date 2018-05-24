import math
x1 = int(input("Digite o x1 "))
y1 = int(input("Digite o y1 "))
x2 = int(input("Digite o x2 "))
y2 = int(input("Digite o y2 "))

dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
if dist >= 10:
	print("longe")
	
else:
	if dist<10:
		print("perto")
