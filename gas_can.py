from boat import Boat
from inheritance_car import InheritanceCar
from motorized_vehicle import MotorizedVehicle

class GasCan :
    def __init__(self, amountLiters) :
        self._amountLiters = amountLiters

    def refill(self, vehicle: MotorizedVehicle) :
        vehicle.refillTank(self._amountLiters)

    # Dont have to do it like this:
#    def refillCar(self, vehicle: InheritanceCar) :
#        vehicle.refillTank(self._amountLiters)

#    def refillBoat(self, vehicle: Boat) :
#        vehicle.refillTank(self._amountLiters)