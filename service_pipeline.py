import pandas as pd

def create_service_record(vehicle_type, damage, intent):

    if intent == "insurance claim":
        priority = "high"

    elif len(damage) > 0:
        priority = "medium"

    else:
        priority = "low"

    return {
        "vehicle_type": vehicle_type,
        "detected_damage": damage,
        "customer_intent": intent,
        "service_priority": priority
    }
