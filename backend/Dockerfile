# Python'ın kararlı ve hafif imajını kullanıyoruz
FROM python:3.10-slim

# Sistem bağımlılıklarını yüklüyoruz (OpenCV ve YOLO için gerekli hafif kütüphaneler)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm backend kodunu kopyala
COPY . .

# FastAPI uygulamasını 8000 portundan dışarı aç
EXPOSE 8000

# Uygulamayı başlat
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]