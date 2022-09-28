from textual.app import App


class Beeper(App):
    def on_key(self):
        # self.console.bell()
        self.console.print('some text here')
        it will print from bottom up, accumulatively.
        


Beeper.run()