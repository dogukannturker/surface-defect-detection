from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.detection_service import DetectionService

app = FastAPI(title="Mini Yüzey Hatası Tespit Uygulaması")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_session = {
    "is_running": False,
    "product_name": "",
    "product_id": "",
    "threshold": 0.25,
    "selected_model": "Mock_Mode",
    "detected_errors": []
}

detector = DetectionService()

@app.post("/api/start")
def start_detection(product_name: str, product_id: str, model_name: str = "Mock_Mode", threshold: float = 0.25):
    current_session["is_running"] = True
    current_session["product_name"] = product_name
    current_session["product_id"] = product_id
    current_session["threshold"] = threshold
    current_session["selected_model"] = model_name
    
    detector.change_model(model_name)
    return {"status": "started"}

@app.post("/api/stop")
def stop_detection():
    current_session["is_running"] = False
    return {"status": "stopped"}

@app.post("/api/reset")
def reset_detection():
    current_session["is_running"] = False
    current_session["product_name"] = ""
    current_session["product_id"] = ""
    current_session["detected_errors"] = []
    return {"status": "reset"}

@app.get("/api/stream")
def stream_detection():
    if not current_session["is_running"]:
        return {"status": "idle", "all_errors": current_session["detected_errors"]}
    
    new_hits = detector.analyze_surface(threshold=current_session["threshold"])
    if new_hits:
        current_session["detected_errors"].extend(new_hits)
        
    return {
        "status": "running", 
        "active_model": current_session["selected_model"],
        "latest_errors": new_hits, 
        "all_errors": current_session["detected_errors"]
    }

@app.get("/api/report")
def generate_report():
    errors = current_session["detected_errors"]
    return {
        "product_name": current_session["product_name"],
        "product_label": current_session["product_id"],
        "threshold": current_session["threshold"],
        "total_defects": len(errors),
        "defects_summary": [{"type": e["defect_type"], "meter": e["meter"]} for e in errors]
    }