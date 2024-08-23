import os
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv

# Caminho para o arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../contexts/.env')

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path)

# Configuração da API
KEY_GEMINI = os.getenv("GOOGLE_API_KEY")
if not KEY_GEMINI:
    raise ValueError("A chave da API do Google não foi encontrada. Verifique o arquivo '.env' na pasta 'contexts'.")

genai.configure(api_key=KEY_GEMINI)

# Modelo de análise de sentimento
model = genai.GenerativeModel('gemini-pro')

def analisar_sentimento(texto):
    try:
        # Gerando a análise do sentimento
        response = model.generate_content(f"Analise o sentimento do seguinte comentário: '{texto}'. Responda com 'negativo', 'neutro' ou 'positivo'.")
        return response.text.strip().lower()
    except Exception as e:
        print(f"Erro ao analisar o comentário: {e}")
        return "erro"

# Função para processar o CSV em chunks
def processar_csv_em_chunks(input_file, output_file, chunksize=1000):
    for chunk in pd.read_csv(input_file, chunksize=chunksize):
        chunk['analise'] = chunk['comment'].apply(analisar_sentimento)
        chunk.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)

# Caminho dos arquivos
input_file = os.path.join(os.path.dirname(__file__), 'input.csv')
output_file = os.path.join(os.path.dirname(__file__), 'arquivo_analisado.csv')

# Processar o arquivo CSV
processar_csv_em_chunks(input_file, output_file)

print(f"Análise de sentimento concluída e salva em '{output_file}'")

# Se quiser salvar em Excel, use:
# df.to_excel('arquivo_analisado.xlsx', index=False)
