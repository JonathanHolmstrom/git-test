from unicycle import Unicycle
from bicycle import Bicycle
from vehicle import Vehicle
from motorized_vehicle import MotorizedVehicle
from boat import Boat
from gas_can import GasCan
from inheritance_car import InheritanceCar
from wheel import Wheel

leftWheel = Wheel(10)
rightWheel = Wheel(20)
testCar = InheritanceCar("V8", [leftWheel, rightWheel])
testCar.drive()
testCar.turnWheel()

# test polymorphism
testGas = GasCan(100)
testBoat = Boat("V12")
testMotorizedVehicle = MotorizedVehicle("Engine")

testGas.refill(testMotorizedVehicle)
testGas.refill(testCar)
testGas.refill(testBoat)

# works in Python but will crash in C++/Java
# DONT DO THIS (instantiate a object of an abstract class)
testVehicle = Vehicle()
testVehicle.getName()


testBike = Bicycle()
testBike.turn()

testCar.turnWheel()

testUnicycle = Unicycle()
testUnicycle.drive()