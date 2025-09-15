"""

Smart Parking System:
• Create classes Vehicle, ParkingSpot, and ParkingLot.
• Create multiple objects (vehicles, spots, parking lot).
• Demonstrate object creation, attribute initialization, and method calls.
• Make sensitive attributes private (e.g., license plate, owner name, spot status).
• Provide getter/setter methods to access/update them safely.
• Show that direct access fails but methods work.
• Vehicle is the base class.
• Derived classes:
    Bike (extra attribute: helmet_required)
    Car (extra attribute: seats)
    SUV (extra attribute: four_wheel_drive)
    Truck (extra attribute: max_load_capacity)
• Each child class overrides display() to print its own details.
• Create a list of different vehicle objects (Bike, Car, SUV, Truck).
• Iterate and call display() → each object responds differently.
• Implement a calculate_parking_fee() method:
    Bike → ₹20/hour
    Car → ₹50/hour
    SUV → ₹70/hour
    Truck → ₹100/hour


• Demonstrate runtime polymorphism by calling the method on different objects.
• Create an abstract class/interface Payment (using abc module).
• Define an abstract method process_payment(amount).
• Create child classes:
    CashPayment
    CardPayment
    UPIPayment
• Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).


Task 1: Vehicle Classes
Implement base and derived vehicle classes with encapsulation.
Override display() and calculate_parking_fee().


Task 2: ParkingSpot Class
Implement ParkingSpot with size restrictions (S, M, L, XL).
Methods: assign_vehicle(), remove_vehicle().
Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).


Task 3: ParkingLot Class
Store multiple parking spots.
Methods:
add_spot() → add new parking spots.
show_spots() → display all spots and their status.
park_vehicle(vehicle) → find suitable spot and park.
unpark_vehicle(vehicle) → remove from spot and calculate fee.


Task 4: Payment (Abstraction + Polymorphism)
When un-parking a vehicle, calculate fee (based on hours).
Ask user for payment method → process payment using appropriate child class.


Task 5: Main Program
Create a parking lot with mixed spots.
Create multiple vehicle objects.
Park/unpark vehicles.
Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.


Create Parking Lot and Spots

Input (program initialization):
lot = ParkingLot("CityMall Parking")
# Add spots of different sizes
lot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))
Output:
Parking Lot Created: CityMall Parking Total Spots Added: 5 

🟢 Step 2: Create Vehicles
Input:
bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)
Output:
Vehicles Created: Bike → ID: B101, Plate: TS01AB1234, Owner: Rahul 
                  Car  → ID: C201, Plate: TS05CD5678, Owner: Priya 
                  SUV  → ID: S301, Plate: TS09EF9012, Owner: Anjali 
                  Truck→ ID: T401, Plate: TS11XY4455, Owner: Ravi 

🟢 Step 3: Park Vehicles
Input:
lot.park_vehicle(bike1)   # Should go to Spot 1 (S)
lot.park_vehicle(car1)    # Should go to Spot 2 (M)
lot.park_vehicle(suv1)    # Should go to Spot 4 (L)
lot.park_vehicle(truck1)  # Should go to Spot 5 (XL)
lot.show_spots()
Output:
Parking Status:
Spot 1 (S): Occupied → Bike (TS01AB1234)
Spot 2 (M): Occupied → Car (TS05CD5678)
Spot 3 (M): EmptySpot 
4 (L): Occupied → SUV (TS09EF9012)
Spot 5 (XL): Occupied → Truck (TS11XY4455)

🟢 Step 4: Unpark a Vehicle + Payment
Input:
lot.unpark_vehicle(car1, hours=3)   # Car stayed 3 hours 
Output:
Car (TS05CD5678) removed from Spot 2Parking Fee = ₹150 Select Payment Method: 1. Cash 2. Card 3. UPI
Enter choice: 3Paid ₹150 using UPI


🟢 Step 5: Final Status
Input:
lot.show_spots()
Output:
Parking Status:
Spot 1 (S): Occupied → Bike (TS01AB1234)
Spot 2 (M): EmptySpot 3 (M): EmptySpot 4 (L): Occupied → SUV (TS09EF9012)
Spot 5 (XL): Occupied → Truck (TS11XY4455)

"""

from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, v_id, license_plate, owner_name):
        self.v_id = v_id
        self.__license_plate = license_plate
        self.__owner_name = owner_name

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print("Vehicle ID:", self.v_id, "Plate:", self.__license_plate, "Owner:", self.__owner_name)

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, v_id, license_plate, owner_name, helmet_required):
        super().__init__(v_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print("Bike → ID:", self.v_id, "Plate:", self.get_license_plate(), "Owner:", self.get_owner_name())

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, v_id, license_plate, owner_name, seats):
        super().__init__(v_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        print("Car  → ID:", self.v_id, "Plate:", self.get_license_plate(), "Owner:", self.get_owner_name())

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, v_id, license_plate, owner_name, four_wheel_drive):
        super().__init__(v_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print("SUV  → ID:", self.v_id, "Plate:", self.get_license_plate(), "Owner:", self.get_owner_name())

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, v_id, license_plate, owner_name, max_load_capacity):
        super().__init__(v_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print("Truck→ ID:", self.v_id, "Plate:", self.get_license_plate(), "Owner:", self.get_owner_name())

    def calculate_parking_fee(self, hours):
        return 100 * hours


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print("Paid ₹", amount, "in Cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print("Paid ₹", amount, "using Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Paid ₹", amount, "using UPI")


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__vehicle = None

    def is_free(self):
        return self.__vehicle is None

    def assign_vehicle(self, vehicle):
        if self.is_free():
            self.__vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        v = self.__vehicle
        self.__vehicle = None
        return v

    def get_vehicle(self):
        return self.__vehicle


class ParkingLot:
    size_map = {
        "Bike": ["S", "M", "L", "XL"],
        "Car": ["M", "L", "XL"],
        "SUV": ["L", "XL"],
        "Truck": ["XL"]
    }

    def __init__(self, place_name):
        self.place_name = place_name
        self.spots = []
        print("Parking Lot Created:", self.place_name, end=" ")

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def show_spots(self):
        print("\nParking Status:")
        for spot in self.spots:
            if spot.is_free():
                print("Spot", spot.spot_id, "(", spot.size, "): Empty")
            else:
                v = spot.get_vehicle()
                print("Spot", spot.spot_id, "(", spot.size, "): Occupied →", type(v).__name__, "(", v.get_license_plate(), ")")

    def find_spot_for_vehicle(self, vehicle):
        v_type = type(vehicle).__name__
        allowed_sizes = ParkingLot.size_map[v_type]
        for spot in self.spots:
            if spot.is_free() and spot.size in allowed_sizes:
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_spot_for_vehicle(vehicle)
        if spot:
            spot.assign_vehicle(vehicle)
        else:
            print("No suitable spot available!")

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(type(vehicle).__name__, "(", vehicle.get_license_plate(), ") removed from Spot", spot.spot_id)
                print("Parking Fee = ₹", fee)
                print("Select Payment Method: 1. Cash 2. Card 3. UPI")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    CashPayment().process_payment(fee)
                elif choice == 2:
                    CardPayment().process_payment(fee)
                elif choice == 3:
                    UPIPayment().process_payment(fee)
                return
        print("Vehicle not found in this parking lot")


lot = ParkingLot("CityMall Parking")
lot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))
print("Total Spots Added:", len(lot.spots))

bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

print("\nVehicles Created:")
bike1.display()
car1.display()
suv1.display()
truck1.display()

lot.park_vehicle(bike1)
lot.park_vehicle(car1)
lot.park_vehicle(suv1)
lot.park_vehicle(truck1)
lot.show_spots()

print("\n--- Unparking Car after 3 hours ---")
lot.unpark_vehicle(car1, hours=3)

lot.show_spots()
