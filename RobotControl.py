class RobotControl:
    def __init__(self):
        pass
    def move_straight_time(self, motion, speed, time):
        x =0.0
        self.motion = motion
        self.speed = speed
        self.time = time
        if motion == 'forward':
            x= speed
            print("robot is moving in forward direction")
        elif motion == "backward":
            x= -speed
            print("robot is moving in backward direction")
        i= 0
        while(i<=time):
            print(i)
            i+=1
        self.stop_robot()
    def stop_robot(self):
        x= 0.0
        print("stop the robot")
    def turn(self, move):
        self.move = move
        if move == "clockwise":
            print("clockwise direciton")
        elif move== "counterclockwise":
            print("counterclockwise direction")

    def sensor_reading(self):
        pass
mr1 = RobotControl()
mr1.move_straight_time('forward', 5, 5)
mr1.turn("clockwise")

        

