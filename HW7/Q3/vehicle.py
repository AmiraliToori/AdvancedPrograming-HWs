


class Vehicle:
    
    def __init__(self, price: int,
                 cycle: int,
                 speed: float,
                 ) -> None:
        self.price = price
        self.cycle = cycle
        self.speed = speed
    
    def __str__(self) -> str:
        return f'''The price of this vehicle is {self.price} dollars,
and have {self.cycle} cycles, which have {self.speed} speed.'''
                    
    
    def __repr__(self) -> str:
        return f'''{type(self).__name__}, Price: {self.price} 
Cycles: {self.cycle}, Speed: {self.speed}'''
    
    
    def speedup(self, value: int) -> None:
        self.speed += value
        
    
    def brake(self, value: int) -> None:
        self.speed -= value
        




class Bicycle(Vehicle):
    
    def __init__(self, price: int,
                 speed: int,
                 cycle: int,
                 gear: int) -> None:
        super().__init__(price, cycle ,speed)
        self.cycle = 2
        self.gear = gear
    
    def __str__(self) -> str:                     
        return f'''The price of this bicycle is: {self.price},
The speed is: {self.speed},
The number of gears: {self.gear},
The count of cycles: {self.cycle}'''

    def __repr__(self) -> str:
        return f'''{type(self).__name__}, Price: {self.price},
Speed: {self.speed},
Gears: {self.gear}
Cycles: {self.cycle}'''




class Tricycle(Vehicle):
    
    def __init__(self, price:int,
                 speed: int,
                 cycle: int,
                 seat: int) -> None:
        self.cycle = 3
        self.seat = seat
        super().__init__(price, cycle, speed)
        
    def __str__(self) -> str:                     
        return f'''The price of this tricycle is: {self.price},
The speed is: {self.speed},
The number of seats: {self.seat},
The count of cycles: {self.cycle}'''
    
    def __repr__(self) -> str:
        return f'''{type(self).__name__}, Price: {self.price},
Speed: {self.speed},
Seats: {self.seat}
Cycles: {self.cycle}'''
        

        
class Motorcycle(Bicycle):
    
    def __init__(self, price: int,
                 speed: int,
                 gear: int,
                 engine: str,
                 cycle: int,
                 power: int) -> None:
        self.engine = engine
        self.power = power
        super().__init__(price, speed, cycle, gear)
    
    def __str__(self) -> str:                     
        return f'''The price of this motorcycle is: {self.price},
The speed is: {self.speed},
The number of gears: {self.gear},
The count of cycles: {self.cycle}
The Engine Type is: {self.engine}
The Power is: {self.power}'''
                    
    def __repr__(self) -> str:
        return f'''{type(self).__name__}, Price: {self.price},
Speed: {self.speed},
Gears: {self.gear}
Cycles: {self.cycle}
Engine: {self.engine}
Power: {self.power}'''


if __name__ == "__main__":
    
    # vehicle_0 = Vehicle()
    vehicle_1 = Bicycle(1200, 10, 5, 2)
    vehicle_2 = Tricycle(600, 5, 5, 1)
    vehicle_3 = Motorcycle(3500, 200, 5, "Pride", 2, 450)


    parking_lot = [vehicle_1, vehicle_2, vehicle_3]

    print(repr(vehicle_1))
    vehicle_1.speedup(20)
    print(repr(vehicle_1))


    print(repr(vehicle_2))
    # print(str(object=vehicle_2))

    # print(repr(vehicle_3))
    # print(str(vehicle_3))