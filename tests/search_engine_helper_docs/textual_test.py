from rich.text import Text
text = Text("hello world python this is python")
text.on(click="view.toggle('world')")

text.highlight_words('python','bold red')
print(text)