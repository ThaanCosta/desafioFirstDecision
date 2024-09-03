# Usando a imagem oficial do Python como base
FROM python:3.11-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de requisitos
COPY requirements.txt .

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Expondo a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
