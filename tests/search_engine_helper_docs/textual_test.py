from rich.text import Text

text = Text(
    "hello world python this is python", style="green"
)  # there is no style applied.
text.on(click="view.toggle('world')")
from rich.console import Console

console = Console()
highlighted = text.highlight_words(
    ["python"], style="yellow"
)  # but we should not highlight individual letters right?
# so we pass a list of words to be highlighted.
# just a damn number?
console.print(text)  # red.
# now we have color. what else?
# we need interface!
# print(highlighted)

# after successfully bricked my damn lenovo device, i realized that there is nothing good using such a restricted shit.
