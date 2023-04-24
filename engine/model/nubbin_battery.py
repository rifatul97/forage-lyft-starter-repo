from abc import abstractmethod, ABC
from datetime import datetime

from engine.model.battery import Battery


class NubbinBattery(Battery, ABC):

    def __init__(self,last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False
