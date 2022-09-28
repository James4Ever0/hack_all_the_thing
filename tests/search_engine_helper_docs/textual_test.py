from rich.text import Text
text = Text("hello world")
text.on(click="view.toggle('world')")

text.highlight_words('python','')