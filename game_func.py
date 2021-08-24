def gameStart(self):
        self.ids.btn1.opacity = 0
        self.ids.btn2.opacity = 0

def start_move(self):
        self.game_start = True


def game_reset(self):
        self.wall1.pos = ((1.3*self.x1/4)-50,0)
        self.wall2.pos = ((3*self.x1/4)-50,0)
        self.wall3.pos = ((4.5*self.x1/4)-50,0)
        self.wall1u.pos = ((1.3*self.x1/4)-50,350)
        self.wall2u.pos = ((3*self.x1/4)-50,200)
        self.wall3u.pos = ((4.5*self.x1/4)-50,280)
        self.flappywingsb.pos = (83, self.y1/2)
        self.flappywingsf.pos = (85, self.y1/2)
        self.flappybody.pos = (70, (self.y1/2)-13)
        self.score = 0

def reset_button(self):
        self.ids.btn2.disabled = False
        self.ids.btn2.opacity = 1
        self.btn_string = "R E S T A R T"