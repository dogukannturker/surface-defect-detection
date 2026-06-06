import os
import random
from datetime import datetime
from ultralytics import YOLO

class DetectionService:
    def __init__(self):
        # Modellerin proje içindeki yolları
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.model_paths = {
            "YOLOv11n": os.path.join(base_dir, "models", "yolov11_best.pt"),
            "YOLOv26n": os.path.join(base_dir, "models", "yolov26_best.pt")
        }
        self.current_model = None
        self.current_model_name = "Mock_Mode"

    def change_model(self, model_name: str):
        """Arayüzden seçilen modele göre ağırlıkları yükler."""
        path = self.model_paths.get(model_name)
        if path and os.path.exists(path):
            try:
                self.current_model = YOLO(path)
                self.current_model_name = model_name
                print(f"[BAŞARILI] {model_name} modeli yüklendi.")
                return True
            except Exception as e:
                print(f"[HATA] Model yüklenemedi: {e}")
        
        self.current_model = None
        self.current_model_name = "Mock_Mode"
        print(f"[BİLGİ] {model_name} aktif değil, Mock modunda çalışılıyor.")
        return False
            
    def analyze_surface(self, threshold: float = 0.25):
        """Yüzey analizini seçili modele veya mock verilere göre simüle eder."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        simulated_meter = round(random.uniform(1.0, 150.0), 2)
        
        # Eğer aktif bir model yüklenmediyse MOCK (Simüle) veriler üret
        if self.current_model is None:
            mock_defects = ["Çizik", "Leke", "Ezik", "Delik"]
            confidence = round(random.uniform(threshold, 0.99), 2)
            
            if random.random() > 0.4:  # %60 ihtimalle hata bulunsun
                return [{
                    "defect_type": random.choice(mock_defects),
                    "meter": simulated_meter,
                    "confidence": confidence,
                    "timestamp": current_time,
                    "model_used": "Mock_Mode"
                }]
            return []
            
        else:
            # Gerçek PyTorch/YOLO Model tespiti
            # Gerçek akışta kamera/dosya yolu beslenebilir, prototip için mock veya boş imaj ile simüle edilir
            # Test amaçlı boş girdi yerine model çıktısı formatını simüle ediyoruz
            mock_defects = ["Alüminyum Çizik", "Yüzey Lekesi"]
            return [{
                "defect_type": random.choice(mock_defects),
                "meter": simulated_meter,
                "confidence": round(random.uniform(threshold, 0.95), 2),
                "timestamp": current_time,
                "model_used": self.current_model_name
            }]