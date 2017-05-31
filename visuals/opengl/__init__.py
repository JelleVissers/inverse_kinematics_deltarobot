# Note this program is a beta version and does not provide accurate results for visualization.

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class delta:
    def __init__(self):
        pygame.init()
        display = (1200,750)
        pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

        gluPerspective(45,(display[0]/display[1]),0.1,50.0)
        glTranslatef(0.0, 2.6, -10)

    def base_info(self):
        self.base_verticies = (
            (-0.5774,0.1, 1.0),
            ( 0.5774,0.1, 1.0),
            (1.1547, 0.1, 0),
            (-1.1547,0.1, 0),
            (-0.5774,0.1,-1.0),
            ( 0.5774,0.1,-1.0),

            (-0.5774 ,-0.1, 1.0),
            (0.5774  ,-0.1, 1.0),
            (1.1547, -0.1,  0),
            (-1.1547, -0.1, 0),
            (-0.5774 ,-0.1,-1.0),
            (0.5774  ,-0.1,-1.0),
        )

        self.base_surface = (
            (0,1,2,3),
            (3,4,5,2),
            (6,7,8,9),
            (8,9,10,11),

            (0,1,7,6),
            (1,2,8,7),
            (2,5,11,8),
            (5,4,10,11),
            (4,3,9,10),
            (3,0,6,9)
        )

        self.base_collor = (
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1)
        )

        self.base_edges = (
            (0, 1),
            (1, 2),
            (2, 5),
            (3, 4),
            (4, 5),
            (3, 0),

            (6, 7),
            (7, 8),
            (8, 11),
            (9, 10),
            (10,11),
            (9, 6),

            (0, 6),
            (1, 7),
            (2, 8),
            (3, 9),
            (4, 10),
            (5, 11),
        )

    def draw_base(self):
        self.base_info()

        glBegin(GL_QUADS)
        for surface in self.base_surface:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(self.base_collor[x])
                glVertex3fv(self.base_verticies[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.base_edges:
            for vertex in edge:
                glColor3fv((1,1,1))
                glVertex3fv(self.base_verticies[vertex])
        glEnd()

    def platform_info(self,Cx,Cy):
        self.base_verticies = (
            (-0.5774,0.1, 1.0),
            ( 0.5774,0.1, 1.0),
            (1.1547, 0.1, 0),
            (-1.1547,0.1, 0),
            (-0.5774,0.1,-1.0),
            ( 0.5774,0.1,-1.0),

            (-0.5774 ,-0.1, 1.0),
            (0.5774  ,-0.1, 1.0),
            (1.1547, -0.1,  0),
            (-1.1547, -0.1, 0),
            (-0.5774 ,-0.1,-1.0),
            (0.5774  ,-0.1,-1.0),
        )

        self.base_surface = (
            (0,1,2,3),
            (3,4,5,2),
            (6,7,8,9),
            (8,9,10,11),

            (0,1,7,6),
            (1,2,8,7),
            (2,5,11,8),
            (5,4,10,11),
            (4,3,9,10),
            (3,0,6,9)
        )

        self.base_collor = (
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1),
            (0, 1, 1)
        )

        self.base_edges = (
            (0, 1),
            (1, 2),
            (2, 5),
            (3, 4),
            (4, 5),
            (3, 0),

            (6, 7),
            (7, 8),
            (8, 11),
            (9, 10),
            (10,11),
            (9, 6),

            (0, 6),
            (1, 7),
            (2, 8),
            (3, 9),
            (4, 10),
            (5, 11),
        )

    def platform_base(self,Cx,Cy):
        self.base_info()

        glBegin(GL_QUADS)
        for surface in self.base_surface:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(self.base_collor[x])
                glVertex3fv(self.base_verticies[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.base_edges:
            for vertex in edge:
                glColor3fv((1,1,1))
                glVertex3fv(self.base_verticies[vertex])
        glEnd()

    def arm_info(self,xb,yb,xc,yc):
        self.arm_verticies = (
            (-0.5774,0.1, 1.0),
            ( 0.5774,0.1, 1.0),

            (-0.5774,xb , yb),
            (0.5774 ,xb , yb),

            (-0.5774, yc+0.1, xc),
            (0.5774 , yc+0.1, xc),

            (-0.5774, -0.1, 1.0),
            (0.5774, -0.1, 1.0),

            (-0.5774, xb, yb),
            (0.5774, xb, yb),

            (-0.5774, yc-0.1, xc),
            (0.5774, yc-0.1, xc)
        )

        self.arm_edges = (
            (0, 2),
            (1, 3),
            (2, 4),
            (3, 5),

            (6, 8),
            (7, 9),
            (8, 10),
            (9, 11),
        )

    def draw_arm(self,xb,yb,xc,yc):
        self.arm_info(xb,yb,xc,yc)

        glBegin(GL_LINES)
        for edge in self.arm_edges:
            for vertex in edge:
                glColor3fv((1,1,1))
                glVertex3fv(self.arm_verticies[vertex])
        glEnd()

    def update(self,Bx0,By0,Bx1,By1,Bx2,By2,Cx0,Cy0,Cx1,Cy1,Cx2,Cy2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0.3, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.draw_base()
        self.draw_arm(Bx0, By0, Cx0+0.33, Cy0)

        glPushMatrix()
        glRotatef(120,0,1,0)
        self.draw_arm(Bx1, By1, Cx1+0.33, Cy1)
        glPopMatrix()

        glPushMatrix()
        glRotatef(240, 0, 1, 0)
        self.draw_arm(Bx2, By2, Cx2+0.33, Cy2)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

def main():
    Delta = delta()

    while True:
        Delta.update(1,2,1,2,1,2,-0,-5,-0,-5,-0,-5)


if __name__ == "__main__":
    main()