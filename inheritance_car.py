from motorized_vehicle import MotorizedVehicle

class InheritanceCar(MotorizedVehicle) :
    def __init__(self, motor, wheels):
        super().__init__(motor)

        self._wheels = wheels

    def drive(self) : # override
        """ Specific driving instructions for a Car """
        super().drive() # first do the general stuff
        # Then do the specific stuff for a Car

    def refillTank(self, amountLiters): # override
        super().refillTank(amountLiters) # optional
        
        print("Running Car Refill")
        # specific stuff for Car

    def turnWheel(self) :
        """ Exists only in Car, not in MotorizedVehicle """