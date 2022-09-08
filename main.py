from wgpu.gui.auto import WgpuCanvas, run
import pygfx as gfx
import imageio.v2 as imageio

data = imageio.imread("earth.png")

canvas = WgpuCanvas()
renderer = gfx.renderers.WgpuRenderer(canvas)
scene = gfx.Scene()

texture = gfx.Texture(data, dim=2, size=(1000, 500, 1))
geometry = gfx.sphere_geometry(-5)
material = gfx.MeshPhongMaterial()
material.map = gfx.TextureView(texture)
sphere = gfx.Mesh(geometry, material)
scene.add(sphere)

camera = gfx.PerspectiveCamera(70, 16 / 9)
camera.position.set(0, 0, 10)


def animate():
    rot = gfx.linalg.Quaternion().set_from_euler(gfx.linalg.Euler(y=0.01))
    sphere.rotation.multiply(rot)
    renderer.render(scene, camera)
    canvas.request_draw()


if __name__ == "__main__":
    canvas.request_draw(animate)
    run()
