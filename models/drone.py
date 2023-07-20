class Drone:
    def __init__(self, serial_number, model, weight_limit, battery_capacity):
        self.serial_number = serial_number
        self.model = model
        self.weight_limit = weight_limit
        self.battery_capacity = battery_capacity
        self.state = "IDLE"  # Default state is IDLE

    def update_state(self, new_state):
        """Update the state of the drone."""
        self.state = new_state
