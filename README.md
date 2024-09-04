# Parking Lot

Desing parking lot

Expected functionality
* Create parking
* Park vehichle -> color, reg no, type
* Get Available slots
* Get parked vehichles based the color, reg no, type
* Leave vehichle from the parking

park = [-1, -1, -1] -> No cars parked
Park(car, 1, "red")
Park(car, 2, "white")
Park(car, 3, "red")
park = [1, 2, 3]
* Available 0
* Leave 2
* Available [1, -1, 2]
* Get 1 -> Get the details from the vehicle class with refrence to the obj id 1
* Leave 1
* Available [-1, -1, 2] -> nearest parking slot is 1
* Park (car, 1, "white")
* Available -> [1, -1, 2]


# To Run the program
* Clone the repository
* run `python controller.py`