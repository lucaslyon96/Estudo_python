n=int(input("Digite um número inteiro: "))
soma=0

while n%10!=n :
	soma=soma+n%10
	n=n//10
soma=soma+n
print(soma)
