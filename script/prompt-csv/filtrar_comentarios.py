import os
import pandas as pd

# Caminho para o arquivo de saída
output_file = os.path.join(os.path.dirname(__file__), 'arquivo_analisado.csv')

# Função para mapear emojis a classificações
def emoji_para_classificacao(emoji):
    return {
        '🤬': 'muito negativo',
        '☹️': 'negativo',
        '😐': 'neutro',
        '🙂': 'positivo',
        '😀': 'muito positivo'
    }.get(emoji, None)

# Função para filtrar comentários com base na classificação
def filtrar_comentarios(emoji):
    classificacao = emoji_para_classificacao(emoji)
    
    if classificacao is None:
        print("Emoji não reconhecido. Use um dos seguintes: 🤬, ☹️, 😐, 🙂, 😀")
        return

    # Ler o arquivo CSV com os comentários analisados
    df = pd.read_csv(output_file)

    # Filtrar os comentários com base na classificação
    comentarios_filtrados = df[df['analise'] == classificacao]

    # Exibir os comentários filtrados no terminal
    if comentarios_filtrados.empty:
        print(f"Nenhum comentário encontrado para a classificação '{classificacao}'.")
    else:
        print(f"Comentários classificados como '{classificacao}':")
        for comentario in comentarios_filtrados['comment']:
            print(f"- {comentario}")

# Exemplo de uso:
emoji_selecionado = input("Selecione um emoji para filtrar os comentários (🤬, ☹️, 😐, 🙂, 😀): ")
filtrar_comentarios(emoji_selecionado)
