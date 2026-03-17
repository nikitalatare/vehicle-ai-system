import random

vehicle_classes = [
    "car",
    "truck",
    "bus",
    "motorbike",
    "van",
    "pickup",
    "SUV"
]

def detect_vehicle(image_path):
    # dummy prediction (replace later with real model)
    return random.choice(vehicle_classes)
