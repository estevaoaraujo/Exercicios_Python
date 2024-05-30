def valida(nota):
    while True:
        if nota < 0 or nota > 10:
            print('Valor inválido! A nota deve estar entre zero e dez.')
            nota = float(input('Digite uma nota entre zero e dez: '))
        else:
            print(f"Você inseriu a nota {nota}.")
            break  # Interrompe o loop se a nota for válida


nota = float(input('Digite uma nota entre zero e dez: '))
valida(nota)
