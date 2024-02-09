import random

print("Dame la longitud del arreglo")
n=int(input())
print("Dame el numero menor del rango")
a=int(input())
print("Dame el numero mayor del rango")
b=int(input())
A=[n]
for i in range (0, n-1):
	A.append(random.randint(a, b))

print("\nDatos desordenados:")
print(A)
print("-------------------")
cont=0
for j in range(1, len(A)):
	cont=cont+2
	key = A[j]
	cont=cont+1
	i=j-1
	cont=cont+2
	while(A[i]>key and i>=0):
		A[i+1]=A[i]
		cont=cont+1
		i=i-1
		cont=cont+2
	A[i+1]=key
	cont=cont+1

print(A)
print("-------------------")
print(cont)