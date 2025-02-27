from abc import ABC, abstractmethod

from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    # @abstractmethod
    def needs_service(self):
        print("engine = ", self.engine.needs_service())
        print("battery = ", self.battery.needs_service())
        return self.engine.needs_service() or self.battery.needs_service()
