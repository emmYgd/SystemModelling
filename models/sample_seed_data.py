from typing import *
from drone import Drone
from medication import Medication

class SampleSeedData:

    def __init__(self):
        pass

    @staticmethod
    def sample_data():
        # Use dictionaries for fast lookup using serial number as key
        drones: Dict = {}

        # Preloaded data
        preloaded_drones = [
            Drone(serial_number="ABC123", model="Lightweight", weight_limit=500, battery_capacity=80, state="IDLE"),
            Drone(serial_number="XYZ789", model="Middleweight", weight_limit=700, battery_capacity=60, state="IDLE"),
        ]

        preloaded_medications = [
            Medication(name="Medicine A", weight=100, code="M123", image="medication_image.jpg"),
            Medication(name="Medicine B", weight=150, code="M456", image="medication_image.jpg"),
        ]

        # Load preloaded data into the drones dictionary
        for drone in preloaded_drones:
            drones[drone.serial_number] = drone

        return drones