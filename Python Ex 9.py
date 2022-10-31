class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


car = Car("ABC-123", 142,)
print ("The properties of new car are: ")
print (f"Registration Number = {car.registration_number}")
print(f"Maximum Speed = {car.maximum_speed} km/hr")
print(f"Current Speed = {car.current_speed}")
print(f"Travelled Distance = {car.travelled_distance}")


class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = int(maximum_speed)
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        return

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        return


car = Car("ABC-123", "142")
print(f"Registration Number = {car.registration_number}")
print(f"Maximum Speed = {car.maximum_speed} km/hr")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Car speed now: {car.current_speed}km/h")
car.accelerate(-200)
print(f"Car speed now: {car.current_speed}km/h")