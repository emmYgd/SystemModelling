from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

class EventController:
    # init app:
    app = FastAPI()

    def __init__(self):
        pass

    async def startup_event(self):
        # Load preloaded medications into the database
        # This is where you would typically load the data from a database or other storage
        # In this example, we're just updating the temporary storage
        pass

    @classmethod
    async def start_event(cls):
        # Create a background scheduler for battery level check
        scheduler = BackgroundScheduler(cls)
        return scheduler.start()

    @staticmethod
    async def shutdown_event(self, scheduler):
        # Clean up resources
        return scheduler.shutdown()

    @app.on_event("startup")
    async def startup_event(self):
        # Load preloaded medications into the database
        # This is where you would typically load the data from a database or other storage
        # In this example, we're just updating the temporary storage
        pass

    @app.on_event("shutdown")
    async def shutdown_event(self, scheduler):
        # Clean up resources
        scheduler.shutdown()
