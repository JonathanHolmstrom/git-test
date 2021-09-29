from manual_vehicle import ManualVehicle


class Bicycle(ManualVehicle) :
    def __init__(self):
        super().__init__()

    def drive(self):
        print("Code to drive the bicycle")