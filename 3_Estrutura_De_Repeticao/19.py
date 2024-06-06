'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''
maior = 0
menor = 0
soma = 0
qtd_repete = int(input("Repetições: "))

while qtd_repete > 0:
    
    numero = int(input("Número: "))
    soma += numero

    if numero > 0 and numero <=100:
        if numero > maior:
            maior = numero
        else:
            menor = numero    
    else:
        print("Incorreto numeros de 0 a 1000")    

    qtd_repete -=1        

print("Maior valor: ",maior)     
print("Menor valor: ",menor)  
print("Soma total: ", soma) 