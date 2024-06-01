'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

mensagem = ""

if centenas > 0:
    if centenas == 1:
        mensagem += "1 centena"
    else:
        mensagem += f"{centenas} centenas"

if dezenas > 0:
    if centenas > 0:
        mensagem += ", "
    if dezenas == 1:
        mensagem += "1 dezena"
    else:
        mensagem += f"{dezenas} dezenas"

if unidades > 0:
    if centenas > 0 or dezenas > 0:
        if centenas == 0 and dezenas == 0:
            mensagem += " e "
        else:
            mensagem += " e "
    if unidades == 1:
        mensagem += "1 unidade"
    else:
        mensagem += f"{unidades} unidades"

print(f"{numero} = {mensagem}")
