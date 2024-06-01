'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.'''

# População inicial
paisA = 80000
paisB = 200000

# Taxa de crescimento anual
taxa_crescimentoA = 0.03
taxa_crescimentoB = 0.015

anos = 0

while paisA < paisB:
    paisA += paisA * taxa_crescimentoA
    paisB += paisB * taxa_crescimentoB
    anos += 1

print(f"Levará {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
print(f"População final do país A: {int(paisA)}")
print(f"População final do país B: {int(paisB)}")

