from wgpu.gui.auto import WgpuCanvas, run
import pygfx as gfx

from planet import Planet

canvas = WgpuCanvas()
renderer = gfx.renderers.WgpuRenderer(canvas)
scene = gfx.Scene()

planets = [
    Planet("Mercury", 5, (10, 0, -10), (0, 0.01, 0), scene),
    Planet("Venus", 5, (10, 0, 10), (0, 0.01, 0), scene),
    Planet("Earth", 5, (0, 0, 0), (0, 0.01, 0), scene),
    Planet("Mars", 5, (-10, 0, 10), (0, 0.01, 0), scene),
    Planet("Jupiter", 5, (-10, 0, -10), (0, 0.01, 0), scene)
]

camera = gfx.PerspectiveCamera(70, 16 / 9)
camera.position.set(0, 0, 30)

controller = gfx.OrbitController(camera.position.clone())
controller.add_default_event_handlers(renderer, camera)


def update():
    for p in planets:
        p.update()
    controller.update_camera(camera)
    renderer.render(scene, camera)
    canvas.request_draw()


if __name__ == "__main__":
    canvas.request_draw(update)
    run()
