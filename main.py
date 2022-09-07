from pyglet.gl import *

window = pyglet.window.Window(resizable=True)

vertices = [-1, -1,
            1, -1,
            -1, 1,
            1, 1]
vertices_gl_array = (GLfloat * len(vertices))(*vertices)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(2, GL_FLOAT, 0, vertices_gl_array)


@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / float(height), .1, 100)
    return pyglet.event.EVENT_HANDLED

theta = 0

@window.event
def on_draw():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, -1, -10)
    glRotatef(-60, 1, 0, 0)
    glRotatef(theta, 0, 0, 1)
    glScalef(2, 2, 2)
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

def update(x, y):
    global theta
    theta += 1

pyglet.clock.schedule(update, 1/10.0)
pyglet.app.run()
