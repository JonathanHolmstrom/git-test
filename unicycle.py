from manual_vehicle import ManualVehicle

class Unicycle(ManualVehicle) :
    def __init__(self):
        super().__init__()

    def drive(self) :
        """ Drive the unicycle """