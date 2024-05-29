'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''

def verifica(peso):
    excesso = peso - 50
    if excesso > 0:
        multa = excesso * 4.00
        return excesso , multa
    else:
        print('Peso não excedido')
        return 0,0

peso = float(input('Digite peso peixe: '))
excesso, multa = verifica(peso)

if excesso > 0:
    print("João excedeu o limite em", excesso, "quilos.")
    print("Ele deverá pagar uma multa no valor de R$", multa)
else:
    print("João não excedeu o limite de peso de peixes. Não há multa a pagar.")

'''ou   

def calcular_multa(peso):
    limite = 50  
    excesso = max(0, peso - limite)  # Calcula o excesso, usando max para garantir que não seja negativo
    multa = excesso * 4.00  
    return excesso, multa

peso_peixes = float(input("Digite o peso dos peixes trazidos por João (em quilos): "))

excesso, multa = calcular_multa(peso_peixes)

if excesso > 0:
    print("João excedeu o limite em", excesso, "quilos.")
    print("Ele deverá pagar uma multa no valor de R$", multa)
else:
    print("João não excedeu o limite de peso de peixes. Não há multa a pagar.")
'''    