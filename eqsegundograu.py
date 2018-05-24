import math
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
delta = (b**2-4*a*c)
 
if delta > 0:
	x1 = (-b + math.sqrt(delta))/2*a
	x2 = (-b - math.sqrt(delta))/2*a	
	print("as raízes da equação são ", x1," e ",x2)
else:
	if delta == 0:

		x1 = (-b + math.sqrt(delta))/2*a
		print("a raiz desta equação é ",x1)
	else:
		print ("esta equação não possui raízes reais")	
