from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from rich.text import Text

text = Text(
    "hello world python this is python", style="green"
)  # there is no style applied.
text.on(click="view.toggle('world')")

class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello [b]World[/b]", style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(2))
        await self.view.dock(*hovers, edge="top")


HoverApp.run()