# Vehicle Intelligence AI System

A multi-modal AI system that analyzes vehicle images, customer text, and metadata to generate automated vehicle service records.

---

##  Features

- Vehicle Type Detection (Computer Vision)
- Damage Detection using YOLOv8
- Customer Intent Detection (LLM/NLP)
- Multi-modal Data Fusion
- FastAPI Real-time Inference API
- Deployable API (Render / Railway)

---

## Architecture

Input:
- Vehicle Image
- Customer Text
- Metadata

Processing:
- Vehicle Classification
- Damage Detection
- Intent Extraction

--

##Tech Stack

Python

FastAPI

YOLOv8 (Ultralytics)

HuggingFace Transformers

PyTorch

--

Output:
```json
{
  "vehicle_type": "SUV",
  "detected_damage": ["dent"],
  "customer_intent": "insurance claim",
  "service_priority": "high"
}
