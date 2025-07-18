class Car:
    def __init__(self,maxSpeed,speedUnit):
        self.maxSpeed = maxSpeed
        self.speedUnit = speedUnit
    
    def __str__(self):
        return f'Car with the maximum speed of {self.maxSpeed} {self.speedUnit}'

class Boat:
    def __init__(self,maxSpeed):
        self.maxSpeed = maxSpeed
    def __str__(self):
        return f'Boat with the maximum speed of {self.maxSpeed} knots'
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    output = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        # fptr.write("%s\n" % vehicle)
        output.append("%s" % vehicle)
    # fptr.close()
    print(output)