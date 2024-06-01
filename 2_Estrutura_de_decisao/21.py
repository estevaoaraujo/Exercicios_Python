'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo 
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 
2 notas de 100, 
1 nota de 50, 2 nota de 5 
1 nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
3 notas de 100, 
1 nota de 50, 
4 notas de 10, 
1 nota de 5 
4 notas de 1.'''

def modo1():
    saque = int(input('Saque: '))

    if saque % 100 != 0:
        centenas = saque //100
        print(centenas, " nota de 100")
        saque -= centenas * 100

    if saque % 50 != 0:
        dezena = saque // 50
        print(dezena, " nota de 50")
        saque -= dezena * 50

    if saque % 10 != 0:
        dezenas = saque // 10
        print(dezenas, " nota de 10")
        saque -= dezenas * 10

    if saque % 5 !=0:
        unidade = saque // 5
        print(unidade, " nota de 5")
        saque -= unidade * 5

    if saque / 1 !=0:
        unidades = saque // 1
        print(unidades, " nota de 1")

# ou  
def modo2():
    saque = int(input("Digite o valor do saque (mínimo 10 reais, máximo 600 reais): "))

    if saque < 10 or saque > 600:
        print("Valor de saque inválido. O valor deve estar entre 10 e 600 reais.")
    else:
        # Calcular o número de notas de cada valor
        notas_100 = saque // 100
        saque -= notas_100 * 100

        notas_50 = saque // 50
        saque -= notas_50 * 50

        notas_10 = saque // 10
        saque -= notas_10 * 10

        notas_5 = saque // 5
        saque -= notas_5 * 5

        notas_1 = saque // 1

        # Exibir o resultado
        if notas_100 > 0:
            print(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100")
        if notas_50 > 0:
            print(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50")
        if notas_10 > 0:
            print(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10")
        if notas_5 > 0:
            print(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5")
        if notas_1 > 0:
            print(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1")

escolha = int(input(" 0 ou 1: "))

if escolha == 0:
    modo1()
elif escolha == 1:
    modo2()    
else:
    print("incorreto")    