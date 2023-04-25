from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self):
        self.sensors = [0] * 4

    def needs_service(self):
        sum = 0
        for i in self.sensors:
            sum += i
        return sum >= 3