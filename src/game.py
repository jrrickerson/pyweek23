import sge


class Game(sge.dsp.Game):
    """ Global Game class """

    def event_key_press(self, key, char):
        if key == 'escape':
            self.event_close()

    def event_close(self):
        self.end()
