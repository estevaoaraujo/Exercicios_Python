'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''

def entrada ():
    tabuada_de = int(input("Tabuada de : "))
    saida(tabuada_de)

def saida(tabuada_de):
    i = 0
    while i <= 10:
        if tabuada_de > 0 and tabuada_de <=10:
            resutaldo = i * tabuada_de
            print( i ," X ", tabuada_de," = ",resutaldo)
            i+= 1
        else:
            print("Valor incorreto, digite valor de 0 a 10 ")    

entrada()