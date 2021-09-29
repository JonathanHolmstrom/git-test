from vehicle import Vehicle
from abc import abstractmethod

class ManualVehicle(Vehicle) :
    def __init__(self):
        super().__init__()

    @abstractmethod # pass the responsibility of implementing the drive function to the children
    def drive(self) :
        """ Do something general for driving a manual vehicle """

    def turn(self) :
        print("Code for turning the vehicle")