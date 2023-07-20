from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from ..controllers.logic_controller import LogicController
from ..controllers.event_controller import EventController


app = FastAPI()


# fast-api pidantic request param validation:
class Drone(BaseModel):
    serial_number: str
    model: str
    weight_limit: int
    battery_capacity: int
    state: str

class Medication(BaseModel):
    name: str
    weight: int
    code: str
    image: str

# the apis:
@app.post("/drones/register", response_model=Drone)
# LogicController.register_drone(drone: Drone)
pass


@app.post("/drones/{serial_number}/load", response_model=Drone)
# LogicController.load_drone(serial_number: str, medications: List[Medication])
pass


@app.get("/drones/{serial_number}/medications", response_model=List[Medication])
# LogicController.get_loaded_medications(serial_number: str)
pass


@app.get("/drones/available", response_model=List[Drone])
# LogicController.get_available_drones
pass

@app.get("/drones/{serial_number}/battery", response_model=int)
# LogicController.get_drone_battery(serial_number: str)
pass

