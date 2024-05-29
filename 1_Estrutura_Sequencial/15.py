'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''


def entrada():
    horas = int(input("Valor ganho por horas: "))
    mes = int(input("Horas trabalhadas por mes: "))
    return horas , mes

def calcula(horas, mes):
    return horas * mes

def tabela(salario):
    print("+ Salário Bruto : R$ ",salario, "\n-IR (11%) : R$ ",salario * 0.11,"\n-INSS (8%) : R$ ",salario * 0.08, end='')
    print("\n-Sindicato ( 5%) : R$ ",salario * 0.05,"\n= Salário Liquido : R$",salario - (salario * 0.11)-(salario * 0.08)-(salario * 0.05))

horas , mes = entrada()
salario = calcula(horas , mes)
tabela(salario)