from abc import ABC, abstractmethod

from serviceable import Serviceable


class Car(ABC):
    _serviceable: Serviceable
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        # self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service()
