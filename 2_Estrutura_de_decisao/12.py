'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

def leitura():
    valor_hora = float(input("Valor por hora: "))
    horas_trabalhadas = int(input("Horas trabalhadas: "))

    if valor_hora <=0 or horas_trabalhadas <= 0:
        print("Valor zerado e salario negativo é invalido ")
    else:
        salario = valor_hora * horas_trabalhadas
        return salario    

def decisao(salario):
    if salario <= 0:
        print("Valor de salário incorreto.")
        return None
    elif salario <= 900:
        return calculos(salario, 0)
    elif salario <= 1500:
        return calculos(salario, 0.05)       
    elif salario <= 2500:
        return calculos(salario, 0.10)       
    else:
        return calculos(salario, 0.20)

def calculos(salario, taxa_IR):
    IR = salario * taxa_IR
    INSS = salario * 0.10
    FGTS = salario * 0.11
    total_descontos = IR + INSS 
    salario_liquido = salario - total_descontos
    return IR, INSS, FGTS, total_descontos, salario_liquido

def extrato(salario, IR, INSS, FGTS, total_descontos, salario_liquido):
    print("Salário Bruto: R$ ", salario)
    print("(-) IR (", IR * 100, "%) R$ ", IR) 
    print("(-) INSS (10%) R$ ", INSS)    
    print("FGTS (11%) R$ ", FGTS)     
    print("Total de descontos R$ ", total_descontos)    
    print("Salário Liquido: R$ ", salario_liquido) 

# Fluxo principal do programa

salario = leitura()

if salario is not None:
    IR, INSS, FGTS, total_descontos, salario_liquido = decisao(salario)
    extrato(salario, IR, INSS, FGTS, total_descontos, salario_liquido)
