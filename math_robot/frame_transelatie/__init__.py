import numpy as np
import math

class transformation:
    def __init__(self,delta_x,delta_y,delta_z,pitch):
        self.x     = delta_x
        self.y     = delta_y
        self.z     = delta_z
        self.pitch = pitch

    def coordinaten(self,x,y,z):
        new_x = math.cos(math.radians(self.pitch))*x-math.sin(math.radians(self.pitch))*y+self.x
        new_y = math.sin(math.radians(self.pitch))*x-math.cos(math.radians(self.pitch))*y+self.y
        new_z = z+self.z

        return new_x,new_y,new_z

    def get_translation_x(self):
        return self.x

    def get_translation_y(self):
        return self.y

    def get_translation_z(self):
        return self.z

    def get_pitch(self):
        return self.pitch

def main():
    x = 0
    y = 0
    z = 0

    x_delta = 10
    y_delta = 20
    z_delta = 30

    motor1 = transformation(10,0,0,0)
    motor2 = transformation(10, 0, 0, 120)
    motor3 = transformation(10, 0, 0, 240)

    print "motor 1 : \t" + str(motor1.coordinaten(10,1,10))
    print "motor 2 : \t" + str(motor2.coordinaten(10,1,10))
    print "motor 3 : \t" + str(motor3.coordinaten(10,1,10))


if __name__ == '__main__':
    main()