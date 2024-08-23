from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

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
    app.run(debug=True)
