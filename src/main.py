import sge
from sge.gfx import Background, Color
from .game import Game
from .rooms import MainMenu
from .objects.testing import TestPlayer, SmallEnemy


def main():
    sge.game = Game(width=640, height=480, fps=120, window_text='SGE Test')
    background = sge.gfx.Background([], sge.gfx.Color("black"))
    player = TestPlayer(sge.game.width / 2, sge.game.height / 2)
    enemy1 = SmallEnemy('a201', sge.game.width / 200, sge.game.height / 1.2, 50)
    enemy2 = SmallEnemy('b201', sge.game.width / 4, sge.game.height / 1.2, 50)
    sge.game.start_room = MainMenu(
        objects=[player, enemy1, enemy2], background=background)
    sge.game.mouse_visible = False
    sge.game.start()
