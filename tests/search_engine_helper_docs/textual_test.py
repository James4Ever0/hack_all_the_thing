from rich.text import Text
text = Text("hello world python this is python")
text.on(click="view.toggle('world')")

text.highlight_words('python',style='red')
print(text)

# after successfully bricked my damn lenovo device, i realized that there is nothing good using such a restricted shit.