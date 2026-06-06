import os
import random
from datetime import datetime
from ultralytics import YOLO

class DetectionService:
    def __init__(self, model_path: str = None):
        # Eğer gerçek bir model yolu verilirse yükle, yoksa mock modu aktifleştir
        if model_path and os.path.exists(model_path):
            self.model = YOLO(model_path)
            self.is_mock = False
        else:
            self.model = None
            self.is_mock = True
            
    def analyze_surface(self, image_path: str, threshold: float = 0.25):
        """
        Görüntü yolunu alır, belirtilen güvenli eşik değerine göre 
        hata tespiti yapar ve standart formatta sonuç döndürür.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Simüle edilmiş metre bilgisi (üretim bandı akışı gibi)
        simulated_meter = round(random.uniform(1.0, 150.0), 2)
        
        if self.is_mock:
            # Model bulunamazsa veya mock çalıştırılmak istenirse devreye girecek yapı
            mock_defects = ["Çizik", "Leke", "Ezik", "Delik"]
            confidence = round(random.uniform(threshold, 0.99), 2)
            
            # Rastgele hata üretimi simülasyonu
            if random.random() > 0.3:  # %70 ihtimalle hata bulsun
                return [{
                    "defect_type": random.choice(mock_defects),
                    "meter": simulated_meter,
                    "confidence": confidence,
                    "timestamp": current_time
                }]
            return [] # Hata yok
            
        else:
            # Gerçek PyTorch/YOLO Model tespiti
            results = self.model(image_path, conf=threshold)
            detected_defects = []
            
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    # Sınıf adını ve güven skorunu al
                    class_id = int(box.cls[0])
                    defect_name = result.names[class_id]
                    conf_score = float(box.conf[0])
                    
                    detected_defects.append({
                        "defect_type": defect_name,
                        "meter": simulated_meter,
                        "confidence": round(conf_score, 2),
                        "timestamp": current_time
                    })
            return detected_defects