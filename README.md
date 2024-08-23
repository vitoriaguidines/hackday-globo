# Watcher - Análise de Sentimentos com Google Gemini

## Descrição 📄

O **Watcher** é um programa que realiza análise de sentimentos em comentários utilizando a API Google Gemini. O script `script_gemini.py` lê comentários a partir de um arquivo CSV, envia-os para a API Google Gemini para análise de sentimentos, e salva os resultados em um novo arquivo CSV.

O programa é capaz de classificar os comentários como "positivo", "neutro" ou "negativo", facilitando a análise de grandes volumes de dados textuais.

## Estrutura do Projeto 📂

- `index.html` e `page.html`: Arquivos HTML que compõem a interface de usuário da aplicação Watcher.
- `style.css`: Arquivo CSS que estiliza a interface.
- `script_gemini.py`: Script principal que realiza a análise de sentimentos utilizando a API do Google Gemini.
- `.env`: Arquivo de configuração onde você deve armazenar sua chave de API do Google de forma segura.
- `input.csv`: Arquivo CSV contendo os comentários que serão analisados.
- `arquivo_analisado.csv`: Arquivo CSV gerado pelo script com os resultados da análise de sentimentos.

## Instalação 🛠️

### Pré-requisitos ✅

Certifique-se de ter o Python 3.x instalado em seu sistema. Além disso, você precisará instalar algumas bibliotecas Python necessárias para o funcionamento do script.

### Instalando as Dependências 📦

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Unix/Linux/MacOS
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

   Caso você não tenha um arquivo `requirements.txt`, adicione as seguintes linhas ao seu arquivo:

   ```
   google-generativeai
   pandas
   python-dotenv
   ```

   Se não tiver um arquivo `requirements.txt`, você pode instalar as dependências manualmente com:

   ```bash
   pip install google-generativeai pandas python-dotenv
   ```

4. Configure sua chave de API 🔑:

   Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Google:

   ```env
   GOOGLE_API_KEY=AIzaSyBf6J1P-ZSLW5BTlx1Do1HXVBsoySScsE0
   ```

   **Nota:** Substitua o valor acima pela sua chave de API real.

## Como Usar 🚀

1. Certifique-se de ter configurado o arquivo `.env` com sua chave de API.

2. Prepare seu arquivo `input.csv` com os comentários que deseja analisar. O arquivo deve ter uma coluna `comment` contendo os textos dos comentários.

3. Execute o script `script_gemini.py`:

   ```bash
   python script_gemini.py
   ```

4. O script irá processar os comentários e salvar os resultados em um arquivo `arquivo_analisado.csv` na mesma pasta.

## Contribuindo 🤝

Sinta-se à vontade para contribuir com o projeto através de pull requests. Por favor, abra uma issue para discutir as mudanças antes de enviar um PR.

## Licença 📜

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato ✉️

Se você tiver alguma dúvida ou sugestão, fique à vontade para entrar em contato.
