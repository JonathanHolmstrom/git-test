from motorized_vehicle import MotorizedVehicle

class Boat(MotorizedVehicle) :
    def __init__(self, motor):
        super().__init__(motor)

    def refillTank(self, amountLiters): # override
        super().refillTank(amountLiters) # optional
        
        print("Running Boat Refill")
        # specific stuff for boat