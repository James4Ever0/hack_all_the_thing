from textual.app import App


class Beeper(App):
    def on_key(self, event):
        # self.console.bell()
        key = event.key
        # self.console.print('some text here')
        print(dir(key))
        self.console.print(key)
        
        # seems to be a string like thing.
        # will pretty print the dir thing. fuck.
        # it will print from bottom up, accumulatively.
        # but what is the fucking key?


Beeper.run()