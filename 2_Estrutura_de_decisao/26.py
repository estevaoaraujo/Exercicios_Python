'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''


def alcool(pedido):
    if pedido > 0:
        if pedido >= 20:
            pedido = (pedido * 1.90) - 0.03
            return pedido
        else:
            pedido = (pedido * 1.90) - 0.05
            return pedido
    else: 
        return 0
    
def gasolina(pedido):
    if pedido > 0:
        if pedido >= 20:
            pedido = (pedido * 2.50) - 0.04
            return pedido
        else:
            pedido = (pedido * 2.50) -  0.06
            return pedido
    else: 
        return 0    
        
escolha = input("A-álcool, G-gasolina: ")

if escolha == 'a' or escolha == 'A':
    quantidade = int(input("Quantidade: "))
    pedido = alcool(quantidade)
    print("Item:       Alcool ")
    print("Quantidade: ",quantidade, " LT")
    print("Total: ", pedido)
elif escolha == 'G' or escolha == 'g':
    quantidade = int(input("Quantidade: "))
    pedido = gasolina(quantidade)    
    print("Item:       Gasolina ")
    print("Quantidade: ",quantidade, " LT")
    print("Total: ", pedido)
else:
    print("Escolha errada alcool ou gasolina")    