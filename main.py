import math
import random
from kivy.app import App
from kivy.core.image import Texture
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *
from kivy.clock import Clock
from kivy.properties import NumericProperty,StringProperty,ObjectProperty
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image


class MainLayout(RelativeLayout):

    from move import move_flappy,move_wall
    from keyboard_func import _keyboard_closed,_on_keyboard_down,_on_keyboard_up
    from builder import flappy_builder,wall_builder
    from game_func import game_reset,gameStart,reset_button,start_move

    cloud_texture = ObjectProperty(None)

    x1,y1 = (NumericProperty(0), NumericProperty(0))
    
    sound = SoundLoader.load("start_sound.wav")

    btn_string = StringProperty("S T A R T")

    game_over = False
    game_start = False

    wall_speed = dp(2.3)
    flap_speed = dp(1)

    score = NumericProperty(0)


    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            self.bg = Rectangle(source = "skyImg.png")
        self.wall_builder()
        self.flappy_builder()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_down=self._on_keyboard_up)
        Clock.schedule_interval(self.move_wall, 1/60)
        Clock.schedule_interval(self.move_flappy, 1/60)


    def on_size(self, *args):
    
        self.wall1.pos = ((1.3*self.width/4)-50, 0)
        self.wall2.pos = ((3*self.width/4)-50, 0)
        self.wall3.pos = ((4.5*self.width/4)-50, 0)
        self.wall1u.pos = ((1.3*self.width)/4, 350)
        self.wall2u.pos = ((3*self.width)/4, 200)
        self.wall3u.pos = ((4*self.width)/4, 280)
        self.flappywingsb.pos = (83, self.height/2)
        self.flappywingsf.pos = (85, self.height/2)
        self.flappybody.pos = (70, (self.height/2)-13)
        self.wall1u.size = (100, self.height - 350 )
        self.wall2u.size = (100, self.height - 200 )
        self.wall3u.size = (100, self.height - 280)
        self.ids.btn1.size = (100, 100)
        self.ids.btn1.pos = ((self.width/2)-25, (self.height/2)-25)
        self.ids.btn2.size = (100, 100)
        self.ids.btn2.pos = ((self.width/2)-125, (self.height/2)-25)
        self.bg.pos = 0,0
        self.bg.size = self.width, self.height
    

    


    def play_sound(self):
        self.sound = SoundLoader.load("start_sound.wav")
        self.sound.play()
        self.sound.loop = True
        self.ids.btn2.disabled = True    

    def collision(self):
        flappy_x,flappy_y = self.flappybody.pos
        wx1, wy1 = self.wall1.pos
        wxu1, wyu1 = self.wall1u.pos
        wx2, wy2 = self.wall2.pos
        wxu2, wyu2 = self.wall2u.pos
        wx3, wy3 = self.wall3.pos
        wxu3, wyu3 = self.wall3u.pos
        if ((wx1 <= flappy_x+40 <= wx1+100) and (wy1 <= flappy_y+13 <= wy1+250)) or ((wxu1<=flappy_x+41<=wxu1+100) and  (wyu1<=flappy_y+13<=wy1+800)):
            self.sound.stop()
            self.reset_button()
            return True
        if ((wx2<=flappy_x+40<=wx2+100) and (wy2<=flappy_y+13<=wy2+150)) or ((wxu2<=flappy_x+40<=wxu2+100) and (wyu2<=flappy_y+13<=wyu2+800)):
            self.sound.stop()
            self.reset_button()
            return True
        if ((wx3<=flappy_x+40<=wx3+100) and (wy3<=flappy_y+13<=wy3+230)) or ((wxu3<=flappy_x+40<=wxu3+100) and (wyu3<=flappy_y+13<=wyu3+800)):
            self.sound.stop()
            self.reset_button()
            return True
        return False


class FlappyApp(App):
    def build(self):
        return MainLayout()


FlappyApp().run()