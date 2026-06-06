# Mini Yüzey Hatası Tespit Uygulaması Prototi̇pi̇

Bu proje, alüminyum yüzey hatalarının (çizik, leke, ezik vb.) tespit edilmesini ve operatör tarafından raporlanmasını simüle eden modüler bir yazılım prototipidir.

## 🚀 Proje Mimarisi & Model Entegrasyonu
Proje, PDF yönergelerine uygun olarak arayüz ve yapay zeka servisleri tamamen bağımsız olacak şekilde **Modüler Yazılım Mimarisi** ile tasarlanmıştır.

* **Yapay Zeka Servisi (`backend/app/services/detection_service.py`):** PyTorch ve Ultralytics altyapısına doğrudan uyumludur. İçerisinde yer alan `change_model()` fonksiyonu sayesinde, sisteme verilen `yolov11_best.pt` ve `yolov26_best.pt` modelleri çalışma anında (dinamik olarak) yüklenebilir ve tahmin üretebilir. Model dosyaları eksik olduğunda sistem otomatik olarak "Mock Modu"na geçerek operatör akışını kesintisiz simüle eder.

## 🛠️ Teknolojiler
* **Backend:** Python / FastAPI
* **Yapay Zeka:** PyTorch / Ultralytics (YOLO)
* **Frontend:** HTML5 / Tailwind CSS / JavaScript (Native Fetch API)
* **Konteynerleştirme:** Docker & Docker Compose

## 📦 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda veya jüri ortamında tek bir komutla ayağa kaldırmak için Docker Compose kullanabilirsiniz:

```bash
# Projeyi Docker ile derleyin ve başlatın
docker-compose up --build