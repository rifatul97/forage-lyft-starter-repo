from abc import abstractmethod, ABC

from car import Car


class Battery(ABC):

    def needs_service(self):
        pass