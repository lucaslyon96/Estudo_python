n=int(input("Digite o valor de n: "))
i=1
fat=n
while i!=n and n!=0:
	fat=fat*(n-i)
	i=i+1
if n==0:
	fat = 1 
print (fat)

