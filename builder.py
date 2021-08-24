from kivy.graphics import *
def wall_builder(self):
        with self.canvas.before:
            Color(34/255, 139/255, 34/255)
            self.wall1 = Rectangle(size=(100,250))
            self.wall2 = Rectangle(size=(100, 150))
            self.wall3 = Rectangle(size=(100,230))
            self.wall1u = Rectangle()
            self.wall2u = Rectangle()
            self.wall3u = Rectangle()

def flappy_builder(self):
        with self.canvas.before:
            Color(173/255, 216/255, 230/255)
            self.flappywingsb = Rectangle(size=(10, 30))
            Color(48/255, 213/255,200/255)
            self.flappybody = Ellipse(size=(40, 25))
            Color(173/255, 216/255, 230/255)
            self.flappywingsf = Rectangle(size=(10, 30))