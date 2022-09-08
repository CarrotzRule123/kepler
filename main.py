from pyglet.gl import *
import math

def generateSphere(sectorCount, stackCount):
    x, y, z, xy = 0, 0, 0, 0
    sectorStep = 2 * math.pi / sectorCount
    stackStep = math.pi / stackCount
    sectorAngle, stackAngle = 0, 0
    vertices = []
    for i in range(0, stackCount):
        stackAngle = math.pi / 2 - i * stackStep
        xy = math.cos(stackAngle)
        z = math.sin(stackAngle)
        for j in range(0, sectorCount + 1):
            sectorAngle = j * sectorStep
            x = xy * math.cos(sectorAngle)
            y = xy * math.sin(sectorAngle)
            vertices.append(x)
            vertices.append(y)
            vertices.append(z)
  
    indices = []
    k1, k2 = 0, 0
    for i in range(0, stackCount):
        k1 = i * (sectorCount + 1)
        k2 = k1 + sectorCount + 1
        for j in range(0, sectorCount):
            if not i == 0:
                indices.append(k1)
                indices.append(k2)
                indices.append(k1 + 1)
            if not i == (stackCount - 1):
                indices.append(k1 + 1)
                indices.append(k2)
                indices.append(k2 + 1)
            k1 += 1
            k2 += 1
    return vertices, indices

window = pyglet.window.Window(resizable=True)

vertices, indices = generateSphere(20, 20)

indices_gl_array = (GLushort * len(indices))(*indices)
vertices_gl_array = (GLfloat * len(vertices))(*vertices)

glEnableClientState(GL_VERTEX_ARRAY)
vertex_buffer = GLuint(0)
glGenBuffers(1, vertex_buffer)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, vertices_gl_array, GL_STATIC_DRAW)
glVertexPointer(3, GL_FLOAT, 0, None)

glEnableClientState(GL_INDEX_ARRAY)
index_buffer = GLuint(0)
glGenBuffers(1, index_buffer)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index_buffer)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * 2, indices_gl_array, GL_STATIC_DRAW)


@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / float(height), .1, 1000)
    return pyglet.event.EVENT_HANDLED

theta = 0

@window.event
def on_draw():
    global theta
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -10)
    glRotatef(-60, 1, 0, 0)
    glRotatef(theta, 0, 0, 1)
    glScalef(2, 2, 2)
    glDrawElements(GL_TRIANGLE_STRIP, len(indices),  GL_UNSIGNED_SHORT, 0)

def update(x, y):
    global theta
    theta += 1

pyglet.clock.schedule(update, 1/10.0)
pyglet.app.run()
