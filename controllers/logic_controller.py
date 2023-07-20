from typing import *
from fastapi import HTTPException
from ..models.drone import Drone
from ..models.medication import Medication
from ..models.sample_seed_data import SampleSeedData
from ..controllers.event_controller import EventController

class LogicController:

    def __init__(self):
        self.drones = SampleSeedData.sample_data()
        self.scheduler = EventController.start_event()

    @staticmethod
    # background algorithm for checking battery level:
    async def check_battery_level(self, drone: Drone):
        """
        Periodic task to check the battery level of a drone and create an audit event log.

        Args:
            self:
            drone (Drone): The drone object to check the battery level for.
        """
        # Get the current battery level from the drone (simulate battery level decrease)
        drone.battery_capacity -= 1

        # Create an audit event log (simulate saving the log to a database or other storage)
        log = f"Drone {drone.serial_number} - Battery Level: {drone.battery_capacity}%"
        print(log)

    @staticmethod
    async def register_drone(self, drone: Drone):
        """
            Register a new drone.

            Args:
                self:
                drone (Drone): The drone object containing the drone details.

            Returns:
                Drone: The registered drone object.

            Raises:
                HTTPException: If a drone with the same serial number already exists.
            """

        if drone.serial_number in self.drones:
            raise HTTPException(status_code=400, detail="Drone with the same serial number already exists.")

        self.drones[drone.serial_number] = drone
        return drone

    @staticmethod
    async def load_drone(self, serial_number: str, medications: List[Medication]):
        """
        Load medications onto a specific drone.

        Args:
            self:
            serial_number (str): The serial number of the drone.
            medications (List[Medication]): The list of medications to load.

        Returns:
            Drone: The updated drone object.

        Raises:
            HTTPException: If the drone is not found, already loading, battery level is below 25%, or total weight exceeds the weight limit.
        """
        drone = self.drones.get(serial_number)
        if drone is None:
            raise HTTPException(status_code=404, detail="Drone not found.")

        if drone.state == "LOADING":
            raise HTTPException(status_code=400, detail="Drone is already loading.")

        if drone.battery_capacity < 25:
            raise HTTPException(status_code=400, detail="Drone battery level is below 25%.")

        total_weight = sum(medication.weight for medication in medications)
        if total_weight > drone.weight_limit:
            raise HTTPException(status_code=400, detail="Total weight exceeds drone's weight limit.")

        # Perform the actual communication and loading process with the drone here
        # Update the drone's state and other attributes accordingly
        drone.state = "LOADING"

        # Schedule the battery level check task for the drone
        self.scheduler.add_job(self.check_battery_level(drone), "interval", seconds=10, args=(drone,))

        return drone

    @staticmethod
    async def get_loaded_medications(self, serial_number: str):
        """
        Get the loaded medications for a specific drone.

        Args:
            self:
            serial_number (str): The serial number of the drone.

        Returns:
            List[Medication]: The list of loaded medications for the drone.
        """
        # In this example, we return a static list of medications for demonstration purposes
        # In a real scenario, one would retrieve the loaded medications from the drone or a database,
        # this will  include the medication associated with a specific drone per time...
        return preloaded_medications

    @staticmethod
    async def get_available_drones(self):
        """
        Get the list of available drones for loading.

        Returns:
            List[Drone]: The list of available drones.
        """
        # In this example, we return all drones regardless of their state
        # In a real scenario, you would filter the drones based on their availability for loading
        return list(self.drones.values())

    @staticmethod
    async def get_drone_battery(self, serial_number: str):
        """
        Get the battery level for a specific drone.

        Args:
            self:
            serial_number (str): The serial number of the drone.

        Returns:
            int: The battery level of the drone.

        Raises:
            HTTPException: If the drone is not found.
        """
        drone = self.drones.get(serial_number)
        if drone is None:
            raise HTTPException(status_code=404, detail="Drone not found.")

        return drone.battery_capacity
