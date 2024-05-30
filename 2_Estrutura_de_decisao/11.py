'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

def inserir():
    salario = float(input("Sálario: "))
    print('Sálario inserido é: ',salario)
    return salario

def valida(salario):
    percentual = [0.20,0.15,0.10,0.05]
    pagamentos = [280,700,1500]

    if salario <= pagamentos[0]:
        salario_atual = salario + (salario * percentual[0])
        print (f'aumento de {percentual[0]} % novo salario é {salario_atual}' )
    elif salario > pagamentos[0] and salario <= pagamentos[1]:
        salario_atual = salario + (salario * percentual[1]) 
        print (f'aumento de {percentual[1]} % novo salario é {salario_atual}' )
    elif salario > pagamentos[1] and salario <= pagamentos[2]:
        salario_atual = salario + (salario * percentual[2])
        print (f'aumento de {percentual[2]} % novo salario é {salario_atual}' )
    elif salario > pagamentos[2]:
        salario_atual = salario + (salario * percentual[3])
        print (f'aumento de {percentual[3]} % novo salario é {salario_atual}' )
    else:
        print("incorreto")

salario = inserir() 
valida(salario)       