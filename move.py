import math
def move_wall(self, dt):
        if self.score%5==0 and self.score!=0:
            self.wall_speed += 0.001
        x,y = self.wall1.pos
        self.game_over = self.collision()
        if (not self.game_over and self.game_start):
            if (x+100) > 0 :
                x -= self.wall_speed
            else:
                x = self.width
            if (x <=0):
                self.score+=math.ceil(1/47)           
            self.wall1.pos = (x,y)
            self.wall1u.pos = (x, 350) 
            x,y = self.wall2.pos
            if (x+100) > 0:
                x -= self.wall_speed
            else:
                x = self.width 
            if (x<=0):
                self.score+=math.ceil(1/47)        
            self.wall2.pos = (x,y)
            self.wall2u.pos = (x, 200)
            x,y = self.wall3.pos
            if (x+100) > 0:
                x -= self.wall_speed
            else:
                x = self.width
            if (x<=0):
                self.score+=math.ceil(1/47)         
            self.wall3.pos = (x,y)
            self.wall3u.pos = (x, 280)

def move_flappy(self, dt):
        x,y = self.flappywingsb.size
        self.game_over = self.collision()
        if (y > -30 and self.flap_speed > 0) and (not self.game_over and self.game_start):
            y -= self.flap_speed
            if y == -30:
                self.flap_speed = -self.flap_speed
        if (y < 30 and self.flap_speed < 0) and not self.game_over:
            y -= self.flap_speed
            if y == 30:
                self.flap_speed = -self.flap_speed        
        self.flappywingsb.size = (x, y)
        self.flappywingsf.size = (x,y) 
