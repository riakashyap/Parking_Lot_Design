class Car:
    def __init__(self,reg_no,colour):
        self.reg_no = reg_no
        self.colour = colour

class ParkingLot:
    def __init__(self,capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        print(f"Created a parking lot with {capacity} slots")
        
    def park(self,reg_no,colour):
        for i in range(self.capacity):
            if self.slots[i] is None:
                self.slots[i] = Car(reg_no,colour)
                print(f"Allocated slot number: {i + 1}")
                return
        print("Sorry, parking lot is full")
        
    def leave(self,slot_no):
        index = slot_no - 1
        if 0 <= index < self.capacity and self.slots[index] is not None:
            self.slots[index] = None
            print(f"Slot number {slot_no} is free")
        else:
            print("Slot already empty or invalid slot")
            
    def status(self):
        print("Slot No. Registration No Colour -")
        for i,car in enumerate(self.slots):
            if car:
                print(f"{i+1} {car.reg_no} {car.colour}")
        
    def registration_numbers_for_cars_with_colour(self,colour):
        result = []
        for i,car in enumerate(self.slots):
            if car and car.colour.lower()==colour.lower():
                result.append(f"{car.colour} - {car.reg_no}")
                #print(f"{car.colour} - {car.reg_no}")
        print(', '.join(result))
                
    def slot_numbers_for_cars_with_colour(self,colour):
        result = []
        for i,car in enumerate(self.slots):
            if car and car.colour.lower()==colour.lower():
                #print(f"{car.colour} - {i+1} ")
                result.append(f"{car.colour} - {i+1}")
        print(', '.join(result))
                
    def slot_number_for_registration_number(self, reg_no):
        result = []
        for i,car in enumerate(self.slots):
            if car and car.reg_no == reg_no:
                result.append(f"{car.reg_no} - {i+1}")
                #print(f"{car.reg_no} - {i+1}")
        if not result:
            print("Not Found")
        else:
            print(', '.join(result))
        
if __name__ == "__main__":
    lot = ParkingLot(6)
    lot.park("KA-01-HH-1234", "White")
    lot.park("KA-01-HH-9999", "White")
    lot.park("KA-01-P-333", "White")
    lot.leave(2)
    lot.park("KA-01-BB-0001", "Black")
    lot.status()
    lot.registration_numbers_for_cars_with_colour("white")
    lot.slot_numbers_for_cars_with_colour("White")
    lot.slot_number_for_registration_number("KA-01-BB-0001")
    lot.slot_number_for_registration_number("MH-04-AY-1111")
    
