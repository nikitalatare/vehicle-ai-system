from fastapi import FastAPI, UploadFile, File, Form
import shutil

from vehicle_classifier import detect_vehicle
from damage_detector import detect_damage
from intent_classifier import detect_intent
from service_pipeline import create_service_record

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Vehicle AI System Running"}

@app.post("/vehicle-service")

async def vehicle_service(
    image: UploadFile = File(...),
    text: str = Form(...)
):

    image_path = "temp.jpg"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    vehicle_type = detect_vehicle(image_path)

    damage = detect_damage(image_path)

    intent = detect_intent(text)

    result = create_service_record(vehicle_type, damage, intent)

    return result
