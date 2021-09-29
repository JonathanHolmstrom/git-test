from vehicle import Vehicle


class MotorizedVehicle(Vehicle) :
    def __init__(self, motor) :
        self._motor = motor

    def drive(self) : # override, skriver över en funktion som finns i en super/parent-klass
        """ Drives the vehicle forwards """

    def refillTank(self, amountLiters) :
        """ Refills the gas tank of the vehicle """
        print("Running MotorizedVehicle refillTank")