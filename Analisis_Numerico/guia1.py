base = 2.0
sign = -1.0
mantisa = 0.0
sesgo = 1024.0
exponente = 0.0

def printNumber(s,v,b,se,e,m) :
    print(s**v*b**(e-se)*m)

# Ejercicio 2
mantisa = 2**-1 + 2**-4 + 2**-7 + 2**-8
exponente = int('10000001010',2)
print('Ejercicio B : ')
printNumber(sign,1,base,sesgo,exponente,mantisa)

# Ejercicio c
mantisa = 2**-1 + 2**-2 + 2**-3 + 2**-4 + 2**-5 + 2**-6 + 2**-7 + 2**-8 + 2**-9 + 2**-10 + 2**-11
exponente = int('00000101010',2)


print('Ejercicio C : ')
printNumber(sign,0,base,sesgo,exponente,mantisa)

mantisa = 2**-1
exponente = int('10010000001',2)
print('Ejercicio D : ')
printNumber(sign,1,base,sesgo,exponente,mantisa)
