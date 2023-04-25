from abc import ABC

class WilloughbyEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        print(self.current_mileage - self.last_service_mileage)
        return self.current_mileage - self.last_service_mileage > 60000
