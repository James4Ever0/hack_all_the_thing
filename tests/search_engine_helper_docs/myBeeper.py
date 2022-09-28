from textual.app import App


class Beeper(App):
    def on_key(self, event):
        # self.console.bell()
        key = event.key
        # self.console.print('some text here')
        print(dir(key))
        self.console.print(key)
        capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentidier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, 
        # seems to be a string like thing.
        # will pretty print the dir thing. fuck.
        # it will print from bottom up, accumulatively.
        # but what is the fucking key?


Beeper.run()