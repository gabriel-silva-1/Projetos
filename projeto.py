gastoMarco = int(input('Gasto em Março: '))
gastoAbril = int(input('Gasto em Abril: '))
gastoTotal = gastoMarco + gastoAbril
gastoMedio = gastoTotal/2

print(gastoTotal)
print(gastoMedio)

if (gastoMedio > 3000):
    print('Pare de gastar no tigrinho')
else:
    print('Ainda é seguro comprar')
