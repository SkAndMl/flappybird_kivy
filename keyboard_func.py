def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        wfx,wfy = self.flappywingsf.pos
        wbx,wby = self.flappywingsb.pos
        bod_x,bod_y = self.flappybody.pos
        self.game_over = self.collision()
        if keycode[1] == "up" and not self.game_over:
            wfy += 6
            wby += 6
            bod_y += 6
            self.flappybody.pos = bod_x,bod_y
            self.flappywingsb.pos = wbx,wby
            self.flappywingsf.pos = wfx,wfy
        elif keycode[1] == "down" and not self.game_over:
            wfy -= 6
            wby -= 6
            bod_y -= 6
            self.flappybody.pos = bod_x,bod_y
            self.flappywingsb.pos = wbx,wby
            self.flappywingsf.pos = wfx,wfy
        return True

def _on_keyboard_up(self, keyboard, keycode, text, modifiers):
        pass 