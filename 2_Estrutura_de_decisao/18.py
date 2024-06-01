'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

if dia <= 30 and dia >=1 and mes <=12 and mes >= 1 and len(str(ano))==4:
    print(f'{dia}/{mes}/{ano} data valida')

# ou 

from datetime import datetime

data_string = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    data = datetime.strptime(data_string, "%d/%m/%Y")
    print("Data válida!")
except ValueError:
    print("Data inválida!")    