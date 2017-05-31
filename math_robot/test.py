from __future__ import division
import math
import matplotlib.pyplot as plt

def find_hoek_a(A,B,C):
    A_2 = math.pow(A, 2)
    B_2 = math.pow(B, 2)
    C_2 = math.pow(C, 2)

    teller = A_2+C_2-B_2
    noemer = 2*A*C

    value = teller/noemer

    return math.acos(value)

def pytagoras_formule(X,Y):
    X_2 = math.pow(X,2)
    Y_2 = math.pow(Y,2)

    return math.sqrt(X_2+Y_2)

def find_motor_hoek(B,A,X,Y):
    #cosinus regel

    # om voorkomen divide door 0
    X =(X+0.000000000000000001)

    #calculate lenghte of c
    C = pytagoras_formule(X,Y)

    b = math.atan(X/Y)
    a = find_hoek_a(A,B,C)

    hoek =  math.degrees(a-b)

    print "hoek a = " + str(math.degrees(a))
    print "hoek b = " + str(math.degrees(b))
    print "hoek   = " + str(hoek)


    return hoek

def coordinaten_abc(A,B,X,Y):

    hoek_b = find_motor_hoek(A,B,X,Y)

    coordinaten_b = [math.cos(hoek_b)*-A,math.sin(hoek_b)*-A]

    # list for coordinaten
    coordinaten = [[0,0],coordinaten_b,[X,Y]]

    return coordinaten

def split_XY(list):
    x = []
    y = []

    for point in list:
        x.append(point[0])
        y.append(point[1])

    return y,x

def print_lengte(coordinaten):
    delta_X_1 = abs(coordinaten[0][0] - coordinaten[1][0])
    delta_X_2 = abs(coordinaten[1][0] - coordinaten[2][0])

    delta_Y_1 = abs(coordinaten[0][1] - coordinaten[1][1])
    delta_Y_2 = abs(coordinaten[1][1] - coordinaten[2][1])

    print "lengte AB : " + str(pytagoras_formule(delta_X_1, delta_Y_1))
    print "lengte BC : " + str(pytagoras_formule(delta_X_2, delta_Y_2))


def main():
    coordinaten = coordinaten_abc(30,60,0,60)
    print coordinaten

    y,x = split_XY(coordinaten)
    print y
    print x
    print
    print_lengte(coordinaten)
    print

    plt.plot(x,y)
    axes = plt.gca()
    axes.set_xlim([-35,5])
    axes.set_ylim([-70, 10])

    plt.show()

if __name__ == '__main__':
    main()