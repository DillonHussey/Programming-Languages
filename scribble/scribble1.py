import pyglet
window = pyglet.window.Window(1024,720,"Scribble", resizable=False)


@window.event
def on_draw():
    window.clear()


#pass means holding method
def update(dt):
    pass



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update,1.0/60)
    pyglet.app.run()