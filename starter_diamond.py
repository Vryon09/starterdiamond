import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# -------------------------------------------------------------
# Base Geometry: 3D Diamond (Octahedron)
# -------------------------------------------------------------
VERTICES = [
    (0.0, 1.0, 0.0),   # 0: Top tip
    (0.0, -1.0, 0.0),  # 1: Bottom tip
    (1.0, 0.0, 0.0),   # 2: Right
    (0.0, 0.0, 1.0),   # 3: Front
    (-1.0, 0.0, 0.0),  # 4: Left
    (0.0, 0.0, -1.0)   # 5: Back
]

FACES = [
    (0, 2, 3), (0, 3, 4), (0, 4, 5), (0, 5, 2),  # Upper pyramid
    (1, 3, 2), (1, 4, 3), (1, 5, 4), (1, 2, 5)   # Lower pyramid
]

COLORS = [
    (1.0, 0.2, 0.2),  # Red
    (0.2, 1.0, 0.2),  # Green
    (0.2, 0.4, 1.0),  # Blue
    (1.0, 1.0, 0.2),  # Yellow
    (1.0, 0.2, 1.0),  # Magenta
    (0.2, 1.0, 1.0),  # Cyan
    (1.0, 0.6, 0.2),  # Orange
    (0.8, 0.8, 0.8)   # Grey
]

def draw_diamond():
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(FACES):
        glColor3fv(COLORS[i])
        for vertex in face:
            glVertex3fv(VERTICES[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Lab: Geometric Transformations")

    glEnable(GL_DEPTH_TEST)

    # Perspective projection
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Initial Transformation State
    tx, ty, tz = 0.0, 0.0, -6.0
    rx, ry, rz = 0.0, 0.0, 0.0
    scale = 1.0

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # =====================================================
        # TODO 1: Keyboard Input Handling
        # =====================================================
        # Update tx, ty, tz using Arrow Keys and W/S
        # Update rx, ry, rz using X, Y, and Z keys
        # Update scale using '+' and '-' keys (ensure scale stays > 0.1)
        # for example: if keys[pygame.K_LEFT]:  tx -= 0.05 (for translation)
        #              if keys[pygame.K_RIGHT]: tx += 0.05 (for rotation)
        #              if keys[pygame.K_EQUALS] or keys[pygame.K_KP_PLUS]: scale += 0.02 (for scaling)
        # Write your key handlers below:




        # =====================================================

        # Render Scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Apply translation
        glTranslatef(tx, ty, tz)

        # =====================================================
        # TODO 2: Apply Rotation and Scaling to the Matrix
        # =====================================================
        # Apply independent Rotations along X, Y, and Z axes (glRotatef)
        # Apply Scaling (glScalef)
        #
        # Write your transformation calls below:




        # =====================================================

        # Draw object
        draw_diamond()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()