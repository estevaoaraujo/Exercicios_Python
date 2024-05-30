#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def valida(nota):
    while True:
        if nota < 0 or nota >10:
            print('invalido')
            nota = float(input('Digite uma nota entre zero e dez: '))
        else:
            print(f"Você inseriu a nota {nota}.")
            break  # Interrompe o loop se a nota for válida



nota = float(input('Nota: '))

valida(nota)