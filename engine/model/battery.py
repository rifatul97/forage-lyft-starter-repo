from abc import abstractmethod, ABC

from car import Car


class Battery(Car, ABC):

    @abstractmethod
    def needs_service(self):
        return Car.needs_service()