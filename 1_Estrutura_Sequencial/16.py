'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

def calculos(metros_quadrados):
    qtd_pintada = metros_quadrados / 3
    latas = qtd_pintada /18
    if latas % 1 != 0:
        latas = int(latas)+1
    preco = latas * 80
    return latas,preco

medida = int(input("Area metros quadrados: "))
latas,preco = calculos(medida)   
print(f'Quantidade de latas {latas} e o preço é {preco}\n')


import math

def calcula(area):
    litros_necessarios = area / 3
    latas_necessarias = math.ceil(litros_necessarios / 18)
    custo_total = latas_necessarias * 80.00
    return latas_necessarias,custo_total


area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

latas_necessarias,custo_total = calcula(area_a_pintar)

print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
print(f"Preço total: R$ {custo_total:.2f}")
