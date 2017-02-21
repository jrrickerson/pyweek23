from sge.dsp import Object
from sge.gfx import Sprite
from sge import keyboard

from ..config import SPRITE_PATH


class TestPlayer(Object):
    MOVE_SPEED = 2

    def __init__(self, x, y):
        self.up_key = 'w'
        self.down_key = 's'
        self.left_key = 'a'
        self.right_key = 'd'
        testplayer_sprite = Sprite(directory=SPRITE_PATH, name='ship')

        super(TestPlayer, self).__init__(
            x, y, sprite=testplayer_sprite, checks_collisions=False)

    def event_step(self, time_passed, delta_multi):
        """ Implement basic thruster-style movement """
        # Figure out what fraction of a second has passed
        step_factor = time_passed / 1000

        if keyboard.get_pressed(self.up_key):
            self.yvelocity += -1.0 * self.MOVE_SPEED * step_factor
        if keyboard.get_pressed(self.down_key):
            self.yvelocity += 1.0 * self.MOVE_SPEED * step_factor
        if keyboard.get_pressed(self.left_key):
            self.xvelocity += -1.0 * self.MOVE_SPEED * step_factor
        if keyboard.get_pressed(self.right_key):
            self.xvelocity += 1.0 * self.MOVE_SPEED * step_factor
