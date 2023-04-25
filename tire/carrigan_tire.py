from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self):
        self.sensors = [0] * 4
        pass

    def needs_service(self):
        for i in self.sensors:
            if i > 0.9:
                return True
        return False