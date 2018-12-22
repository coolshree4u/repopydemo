class Vehicle:

    def __init__(self,VIN,weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer= manufacturer


    def getWeight(self):
        return  self.weight

    def getManufacturer(self):
        return self.manufacturer

    def VehicleType(self):
        pass

class Truck(Vehicle):
    def __init__(self,VIN,weight, manufacturer,capacity):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.capacity = capacity

    def transportCapacity(self):
        return self.capacity

    def VehicleType(self):
        return 'Truck'


class Car(Vehicle):
    def __init__(self,VIN,weight, manufacturer,seat):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.seat = seat

    def NoumberOfSeat(self):
        return self.seat

    def VehicleType(self):
        return 'Car'

a = Car('ABC1',1000,'BMW', 4)
b= Truck('ABC1',2000,'BMW', 4)


print(a.getManufacturer())
print(b.getWeight())