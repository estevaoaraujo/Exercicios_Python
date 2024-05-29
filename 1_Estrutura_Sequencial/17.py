'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.'''

def calcular_tinta(area):
    # Acrescentar 10% de folga
    area_com_folga = area * 1.1
    litros_necessarios = area_com_folga / 6
    return litros_necessarios

def arredondar_para_cima(valor):
    if valor % 1 != 0:
        return int(valor) + 1
    return int(valor)

def calcular_latas(litros):
    # Cada lata tem 18 litros
    latas = litros / 18
    latas = arredondar_para_cima(latas)
    preco_latas = latas * 80
    return latas, preco_latas

def calcular_galoes(litros):
    # Cada galão tem 3.6 litros
    galoes = litros / 3.6
    galoes = arredondar_para_cima(galoes)
    preco_galoes = galoes * 25
    return galoes, preco_galoes

def calcular_mistura(litros):
    # Mistura de latas e galões para minimizar desperdício
    latas = litros // 18
    restante = litros % 18
    galoes = restante / 3.6
    galoes = arredondar_para_cima(galoes)
    
    # Calcular o custo total
    preco_total = (latas * 80) + (galoes * 25)
    
    return latas, galoes, preco_total

# Entrada de dados
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculos
litros_necessarios = calcular_tinta(area_a_pintar)

# Apenas latas de 18 litros
latas, preco_latas = calcular_latas(litros_necessarios)

# Apenas galões de 3.6 litros
galoes, preco_galoes = calcular_galoes(litros_necessarios)

# Mistura de latas e galões
latas_mistura, galoes_mistura, preco_mistura = calcular_mistura(litros_necessarios)

# Saída de resultados
print(f"\nPara pintar {area_a_pintar:.2f} metros quadrados (com 10% de folga):")
print(f"Usando apenas latas de 18 litros:")
print(f" - Quantidade de latas: {latas}")
print(f" - Preço total: R$ {preco_latas:.2f}")

print(f"\nUsando apenas galões de 3.6 litros:")
print(f" - Quantidade de galões: {galoes}")
print(f" - Preço total: R$ {preco_galoes:.2f}")

print(f"\nMisturando latas e galões para minimizar o desperdício:")
print(f" - Quantidade de latas: {int(latas_mistura)}")
print(f" - Quantidade de galões: {galoes_mistura}")
print(f" - Preço total: R$ {preco_mistura:.2f}")

