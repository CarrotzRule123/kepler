import imageio.v2 as imageio
import pygfx as gfx


class Planet:
    def __init__(self, name, radius, position, spin, scene):
        self.name = name
        self.radius = radius
        self.position = position
        self.spin = spin
        self.object = self.add_object(scene)

    def add_object(self, scene):
        data = imageio.imread("textures/" + self.name + ".png")
        texture = gfx.Texture(data, dim=2, size=(2048, 1024, 1))
        geometry = gfx.sphere_geometry(-self.radius)
        material = gfx.MeshPhongMaterial()
        material.map = gfx.TextureView(texture)
        object = gfx.Mesh(geometry, material)
        scene.add(object)
        return object

    def update(self):
        rot = gfx.linalg.Quaternion().set_from_euler(gfx.linalg.Euler(*self.spin))
        self.object.rotation.multiply(rot)
        self.object.position.set(*self.position)
