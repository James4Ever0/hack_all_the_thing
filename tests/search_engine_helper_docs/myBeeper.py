from textual.app import App


class Beeper(App):
    def on_key(self, event):
        # self.console.bell()
        key = event.key
        # self.console.print('some text here')
        self.console.print(key, dir(key))
        # will pretty print the dir thing. 
        # it will print from bottom up, accumulatively.
        # but what is the fucking key?


Beeper.run()