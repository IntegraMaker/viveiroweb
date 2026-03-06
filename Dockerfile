FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY viveiroweb/ /app/

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=viveiroweb.settings

# Cria diretórios para static files e media
RUN mkdir -p /app/staticfiles /app/imagens/media

# Expõe a porta 8000
EXPOSE 8000

# Define o diretório de trabalho para onde está o manage.py
WORKDIR /app

# Comando para executar a aplicação com Gunicorn
CMD ["gunicorn", "viveiroweb.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
