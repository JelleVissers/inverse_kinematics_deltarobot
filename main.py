from visuals import opengl
from math_robot import frame_transelatie
import math_robot as mr

coordinaten = (0,0,-40) #cm

# lengte van de verschillende armen
A = 20 #cm
B = 50 #cm

# initaliseer coordinten van motoren
motor1 = frame_transelatie.transformation(1,0,0,0)
motor2 = frame_transelatie.transformation(1,0,0,120)
motor3 = frame_transelatie.transformation(1,0,0,240)

# calculate the coordinaten of the different motors
coordinaten_motor1 = motor1.coordinaten(coordinaten[0],coordinaten[1],coordinaten[2])
coordinaten_motor2 = motor2.coordinaten(coordinaten[0],coordinaten[1],coordinaten[2])
coordinaten_motor3 = motor3.coordinaten(coordinaten[0],coordinaten[1],coordinaten[2])

# print coordinaten tenopzichten van de motoren
print "coordinaten_motor1\t=\t%s"%(str(coordinaten_motor1))
print "coordinaten_motor2\t=\t%s"%(str(coordinaten_motor2))
print "coordinaten_motor3\t=\t%s\n"%(str(coordinaten_motor3))


# bereken hoek #
motorhoek_1 = mr.hoek_motor(A,B,coordinaten_motor1[0],coordinaten_motor1[2])
motorhoek_2 = mr.hoek_motor(A,B,coordinaten_motor2[0],coordinaten_motor2[2])
motorhoek_3 = mr.hoek_motor(A,B,coordinaten_motor3[0],coordinaten_motor3[2])

if motorhoek_1 > 90:
   motorhoek_1 = motorhoek_1-90

if motorhoek_2 > 90:
   motorhoek_2 = motorhoek_2-90

if motorhoek_3 > 90:
   motorhoek_3 = motorhoek_3-90

# print de hoeken A
print "motor hoek 1\t\t=\t%f\tgraden"%(motorhoek_1)
print "motor hoek 2\t\t=\t%f\tgraden"%(motorhoek_2)
print "motor hoek 3\t\t=\t%f\tgraden\n"%(motorhoek_3)

coordinaten_join_1 = mr.get_coordinaten(A,B,motorhoek_1,coordinaten_motor1[0],coordinaten_motor1[2])
coordinaten_join_2 = mr.get_coordinaten(A,B,motorhoek_2,coordinaten_motor2[0],coordinaten_motor2[2])
coordinaten_join_3 = mr.get_coordinaten(A,B,motorhoek_3,coordinaten_motor3[0],coordinaten_motor3[2])

print "coordinaten 1 A-B_C =\t%s"%(str(coordinaten_join_1))
print "coordinaten 2 A-B_C =\t%s"%(str(coordinaten_join_2))
print "coordinaten 3 A-B_C =\t%s\n"%(str(coordinaten_join_3))

Bx1,Cx1,By1,Cy1 = coordinaten_join_1[0][1],coordinaten_join_1[0][2],coordinaten_join_1[1][1],coordinaten_join_1[1][2],
Bx2,Cx2,By2,Cy2 = coordinaten_join_2[0][1],coordinaten_join_2[0][2],coordinaten_join_2[1][1],coordinaten_join_2[1][2],
Bx3,Cx3,By3,Cy3 = coordinaten_join_3[0][1],coordinaten_join_3[0][2],coordinaten_join_3[1][1],coordinaten_join_3[1][2],

#Delta = opengl.delta()

#while True:
#   Delta.update(-Bx1,By1,-Bx2,By2,-Bx3,By3,Cx1-1,Cy1,Cx2-1,Cy2,Cx3-1,Cy3)

