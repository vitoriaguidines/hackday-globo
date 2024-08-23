from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)

# Permitir apenas as origens específicas
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://192.168.15.8:5500"]}})

# Caminho para o arquivo CSV
csv_file = os.path.join(os.path.dirname(__file__), 'script/prompt-csv/arquivo_analisado.csv')

# Mapeamento de emojis para classificações
emoji_to_classificacao = {
    '🤬': 'muito negativo',
    '☹️': 'negativo',
    '😐': 'neutro',
    '🙂': 'positivo',
    '😀': 'muito positivo'
}

@app.route('/filtrar')
def filtrar_comentarios():
    emoji = request.args.get('emoji')
    classificacao = emoji_to_classificacao.get(emoji)

    if not classificacao:
        return jsonify({"comentarios": []})

    # Ler o CSV e filtrar comentários
    df = pd.read_csv(csv_file)
    comentarios_filtrados = df[df['analise'] == classificacao]['comment'].tolist()

    return jsonify({"comentarios": comentarios_filtrados})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
