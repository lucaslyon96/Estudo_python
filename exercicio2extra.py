segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = segundos//(60*60*24)
segundos = segundos%(60*60*24)
b = segundos//(60*60)
segundos = segundos%(60*60)
c = segundos//(60)s
d = segundos%60

print(a," dias, ",b," horas, ",c," minutos e ",d," segundos.")

