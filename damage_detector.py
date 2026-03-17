from ultralytics import YOLO

# using pretrained YOLO
model = YOLO("yolov8n.pt")

def detect_damage(image_path):

    results = model(image_path)

    damages = []

    for r in results:
        boxes = r.boxes

        if boxes is None:
            return []

        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            damages.append(label)

    return damages
