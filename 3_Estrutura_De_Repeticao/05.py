'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.'''

def obter_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_anos(populacaoA, taxaA, populacaoB, taxaB):
    anos = 0
    while populacaoA < populacaoB:
        populacaoA += populacaoA * (taxaA / 100)
        populacaoB += populacaoB * (taxaB / 100)
        anos += 1
    return anos, populacaoA, populacaoB

while True:
    print("Informe as populações e as taxas de crescimento:")
    populacaoA = obter_valor_positivo("População do país A: ")
    taxaA = obter_valor_positivo("Taxa de crescimento anual do país A (%): ")
    populacaoB = obter_valor_positivo("População do país B: ")
    taxaB = obter_valor_positivo("Taxa de crescimento anual do país B (%): ")

    anos, populacaoA_final, populacaoB_final = calcular_anos(populacaoA, taxaA, populacaoB, taxaB)

    print(f"Levará {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
    print(f"População final do país A: {int(populacaoA_final)}")
    print(f"População final do país B: {int(populacaoB_final)}")

    repetir = input("Deseja repetir a operação? (s/n): ").strip().lower()
    if repetir != 's':
        break
