
from car import Car
class ParkingLot:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.parking = [-1] * capacity
        self.occupied_slots = 0

    def __repr__(self) -> str:
        return str(self.__dict__)

    def park(self, vehicle) -> bool:
        """
        Check available slot
        if yes park
        else return parking full
        """

        if isinstance(vehicle, int):
            raise ValueError("Vehichle should be not be integer class instance")

        if isinstance(vehicle, str):
            raise ValueError("Vehichle should be not be string class instance")

        # print("Occupied slots",self.occupied_slots)
        if self.occupied_slots == self.capacity:
            print("Parking full")
            return False
        for index in range(len(self.parking)):
            if self.parking[index] != -1:
                continue
            else:
                print("slot", index)
                self.parking[index] = vehicle
                self.occupied_slots += 1
                print("Parked vehicle", vehicle)
                break
        return True

    def leave_parking(self, vehicle_obj):
        for index, vehicle in enumerate(self.parking):
            if vehicle.reg_no == vehicle_obj.reg_no and vehicle.color == vehicle_obj.color:
                self.parking[index] = -1
                print("Vehichle {0} left parking".format(vehicle_obj))
                return True
        print("Vehicle not there in parking")


    def get_by_reg_no(self, reg_no):
        for vehicle in self.parking:
            if vehicle.reg_no == reg_no:
                return vehicle
        return "Vehicle does not exists in parking"



car1 = Car("White", "MH12-RW-3846", "Bike")
car2 = Car("Black", "MH12-RW-3845", "Car")
car3 = Car("Red", "MH12-RW-3844", "Car")

parking_obj = ParkingLot(2)
parking_obj.park(car1)
parking_obj.park(car2)
parking_obj.leave_parking(car3)
print(parking_obj.parking)
print("get by reg no", car1.reg_no)
print(parking_obj.get_by_reg_no(car3.reg_no))