import google.generativeai as genai
import pandas as pd
import os

# Configuração da API
KEY_GEMINI = "AIzaSyBf6J1P-ZSLW5BTlx1Do1HXVBsoySScsE0"
os.environ['GOOGLE_API_KEY'] = KEY_GEMINI
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Modelo de análise de sentimento
model = genai.GenerativeModel('gemini-pro')

def analisar_sentimento(texto):
    # Gerando a análise do sentimento
    response = model.generate_content(f"Analise o sentimento do seguinte comentário: '{texto}'. Responda com 'negativo', 'neutro' ou 'positivo'.")
    return response.text.strip().lower()

# Leitura do arquivo (substitua 'arquivo.csv' pelo caminho do seu arquivo)
# Para CSV
df = pd.read_csv('input.csv')

# Se for um arquivo Excel, use:
# df = pd.read_excel('arquivo.xlsx')

# Analisando a coluna "comment" e criando a coluna "analise"
df['analise'] = df['comment'].apply(analisar_sentimento)

# Salvando o resultado em um novo arquivo CSV
df.to_csv('arquivo_analisado.csv', index=False)

# Se quiser salvar em Excel, use:
# df.to_excel('arquivo_analisado.xlsx', index=False)

print("Análise de sentimento concluída e salva em 'arquivo_analisado.csv'")
