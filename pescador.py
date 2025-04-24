"""
JOÃO PAPO-DE-PESCADOR

João Papo-de Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

João precisa que você faça um program que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa qie João deverá pagar. Imprima os dados do programa com as mensagens adequadas
"""
peso_maximo = 50
aliquota = 4
peso_de_peixes = int(input("Digite o peso do pescado: "))

if peso_de_peixes > peso_maximo:
    excesso = peso_de_peixes - peso_maximo
    multa = excesso * aliquota
    print(f"Você irá precisar pagar R${multa} de multa")
else:
    print("Você não irá precisar pagar multa")
