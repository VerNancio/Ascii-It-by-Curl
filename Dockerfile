# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crie um ambiente virtual
RUN python -m venv venv

# Ative o ambiente virtual e instale as dependências Python
RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . .

# Ative o ambiente virtual por padrão
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Comando para iniciar o aplicativo (substitua conforme necessário)
CMD ["python", "app.py"]
