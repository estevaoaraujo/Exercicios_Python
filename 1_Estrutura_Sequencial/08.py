#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Recebimentos em horas: '))
horas_mes = int(input('Horas trabalhadas: '))
total = horas_mes *valor_hora
print(f'{total} R$')