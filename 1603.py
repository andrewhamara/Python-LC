class ParkingSystem:

    b, m, s = 0, 0, 0

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                self.b -= 1
                return self.b > -1
            case 2:
                self.m -= 1
                return self.m > -1
            case 3:
                self.s -= 1
                return self.s > -1
