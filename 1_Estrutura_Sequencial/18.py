'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

def calcular_tempo_download(tamanho_arquivo_mb, velocidade_mbps):
    # Converter tamanho do arquivo de MB para megabits (Mb)
    tamanho_arquivo_mb = float(tamanho_arquivo_mb)
    velocidade_mbps = float(velocidade_mbps)
    
    tamanho_arquivo_mb *= 8  # 1 MB = 8 Megabits (Mb)
    
    # Calcular o tempo de download em segundos
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_mbps
    
    # Converter o tempo de download para minutos
    tempo_download_minutos = tempo_download_segundos / 60
    
    return tempo_download_minutos

# Entrada de dados
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Cálculo do tempo de download
tempo_download_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_mbps)

# Exibição do resultado
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
