from __future__ import division

import math
import matplotlib.pyplot as plt

def hoek_a(A,B,C):
    A_2 = math.pow(A,2)
    B_2 = math.pow(B,2)
    C_2 = math.pow(C,2)

    noemer = A_2+C_2-B_2
    teller = 2*A*C

    return math.degrees(math.acos(noemer/teller))

def lengte_c(X,Y):
    return math.sqrt(math.pow(X,2)+math.pow(Y,2))

def hoek_c(X,Y):
    return math.degrees(math.atan(X/Y))

def hoek_motor(A,B,X,Y):
    C = lengte_c(X,Y)
    value_hoek_a = hoek_a(A,B,C)
    value_hoek_c = hoek_c(X,Y)

    return value_hoek_a+value_hoek_c

def get_coordinaten(A,B,motorhoek,X,Y):
    x = [0]
    y = [0]

    x.append(math.sin(math.radians(motorhoek))*A)
    y.append(math.cos(math.radians(motorhoek))*A)

    x.append(X)
    y.append(Y)

    return x,y

def print_length(X_list,Y_list):

    delta_Ax = abs(X_list[0] - X_list[1])
    delta_Ay = abs(Y_list[0] - Y_list[1])

    delta_Bx = abs(X_list[1] - X_list[2])
    delta_By = abs(Y_list[1] - Y_list[2])

    print "Lengte A : \t"+str(math.sqrt(math.pow(delta_Ax,2)+math.pow(delta_Ay,2)))
    print "Lengte B : \t"+str(math.sqrt(math.pow(delta_Bx,2)+math.pow(delta_By,2)))


def main():
    A = 30
    B = 60

    X = 0
    Y = 80


    motorhoek   = hoek_motor(A,B,X,Y)
    x,y         = get_coordinaten(A,B,motorhoek,X,Y)
    print_length(x,y)

    print x
    print y

    plt.plot(x,y)

    plt.show()



if __name__ == '__main__':
    main()