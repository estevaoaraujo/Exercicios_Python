'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                  Até 5 Kg              Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

def menu():
    print("--------Fruteira-------")
    print(" 1 - Maça ")
    print(" 2 - Morango ")

def pedido_maca(pedido):
    if pedido <= 5:
        pedido *= 1.80
        return pedido 
    
    elif pedido > 5:
        pedido *= 1.50
        if pedido >= 25.00:
            pedido -= (pedido * 0.10 )
            return pedido     
        return pedido 

def pedido_norango(pedido):
    if pedido <= 5:
        pedido *= 2.50
        return pedido
    
    elif pedido > 5:
        pedido *= 2.20
        if pedido >= 25.00:
            pedido -= (pedido * 0.10 ) 
            return pedido            

quantidade = float(input("Quantidade: "))

if quantidade > 0:
    escolha = int(input("Maça ou morando: "))
    if escolha == 1:
        pedido = pedido_maca(quantidade)
        print("Item: Maça")
        print("Preço: ", pedido)
    elif escolha == 2:
        pedido = pedido_norango(quantidade)
        print("Item: Morango")
        print("Preço: ", pedido)            
    else:
        print("Escolha incorreta")    
else:
    print("Quantidade insuficiente")        