from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from rich.text import Text
# from rich.table import Table
from textual.layouts.vertical import VerticalLayout
# text = Text(
#     "hello world python this is python", style="green"
# )  # there is no style applied.
# import os
# text.on(click="os.system('bash less_jump_to_line.sh')") # what is this fucking toggle?
# text.on(click="view.toggle('world')") # what is this fucking toggle?
# text.on(click=lambda: os.system('bash less_jump_to_line.sh')) # unmarshallable. fuck.
# text.on(click="view.toggle('side')")


class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        text = Text(self.name)
        import os
        size = os.get_terminal_size()
        width = size.columns-1
        return Panel(
            text, style=("on red" if self.mouse_over else ""), height=4, width = width
        )  # this is arguable. maybe for mobile device this will be different?
        # calculate this height according to terminal width, and make sure it does not go lower than 3.

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_click(self):
        # if self.name == "widget 1":
        #     # import os
        #     # command = 'bash less_jump_to_line.sh'
        #     # os.system(command) # does not work properly! fuck.
        # else:
        print("CLICKED {}".format(self.name))
        breakpoint()


from textual.widgets import ScrollView


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        # self.hovers = (
        #     Hover(
        #         "widget {}".format(index),
        #     )
        #     for index in range(3)
        # )
        self.scrollableHovers = ScrollView()  # with name or not? you need keywords.
        # hoverRenderable = self.hovers
        self.layout = VerticalLayout()

        # self.renderableHovers = Table()
        for index in range(3): # this is bad. these things are not clickable.
            self.layout.
        #     self.renderableHovers.add_row(
        #         Hover(
        #             "widget {}".format(index),
        #         )
        #     )

        await self.scrollableHovers.update(self.renderableHovers)
        await self.view.dock(self.scrollableHovers, edge="top", name="side")  # WTF?
        # here we got the view.

    # async def on_load(self) -> None:


HoverApp.run()
