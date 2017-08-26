import pyglet

mainWindow = pyglet.window.Window()

characterWindow = pyglet.window.Window()

mainWindowText = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=mainWindow.width//2, y=mainWindow.height//2,
                          anchor_x='center', anchor_y='center')

characterWindowText = pyglet.text.Label('Hi I am character',
                          font_name='Times New Roman',
                          font_size=36,
                          x=characterWindow.width//2, y=characterWindow.height//2,
                          anchor_x='center', anchor_y='center')

@mainWindow.event
def on_draw():
    mainWindow.clear()
    mainWindowText.draw()

@characterWindow.event
def on_draw():
    characterWindow.clear()
    characterWindowText.draw()


pyglet.app.run()
