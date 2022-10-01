from rich.panel import Panel


# https://github.com/Cvaniak/TextualListViewUnofficial
# the hack
# pip3 install git+https://github.com/Cvaniak/TextualListViewUnofficial.git
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from rich.text import Text

from textual.widgets import ScrollView

# text = Text(
#     "hello world python this is python", style="green"
# )  # there is no style applied.
# import os
# text.on(click="os.system('bash less_jump_to_line.sh')") # what is this fucking toggle?
# text.on(click="view.toggle('world')") # what is this fucking toggle?
# text.on(click=lambda: os.system('bash less_jump_to_line.sh')) # unmarshallable. fuck.
# text.on(click="view.toggle('side')")
from ck_widgets_lv import ListViewUo


class Hover(Widget):

    mouse_over = Reactive(False)

    def __init__(self, *args, **kwargs):
        self.clickFunction = kwargs.get('onClick', None)
        super().__init__(*args, **kwargs)

    def render(self) -> Panel:
        text = Text(self.name)
        import os

        size = os.get_terminal_size()
        width = size.columns - 1
        return Panel(
            # this style is strange. we should alter it in some way.
            text, style=("on red" if self.mouse_over else ""), height=4, width=width
        )  # this is arguable. maybe for mobile device this will be different?
        # calculate this height according to terminal width, and make sure it does not go lower than 3.

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_click(self):
        if self.clickFunction:
            self.clickFunction() # what should you pass?
        # if self.name == "widget 1":
        #     # import os
        #     # command = 'bash less_jump_to_line.sh'
        #     # os.system(command) # does not work properly! fuck.
        # else:
        # print("CLICKED {}".format(self.name))
        # breakpoint()


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        # self.hovers = (
        #     Hover(
        #         "widget {}".format(index),
        #     )
        #     for index in range(3)
        # )
        self.mainViewer = ScrollView()  # with name or not? you need keywords.
        # hoverRenderable = self.hovers
        await self.mainViewer.update(Text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '*20))
        # self.renderableHovers = Table()
        self.scrollableHovers = ListViewUo(
            [
                # this is bad. these things are not clickable.
                Hover(
                    "widget {}".format(index),onClick = lambda: self.view.toggle()
                )
                for index in range(30)
            ]
        )
        #     self.renderableHovers.add_row(
        #         Hover(
        #             "widget {}".format(index),
        #         )
        #     )

        await self.view.dock(self.scrollableHovers, edge="top", name="side")  # WTF?
        await.self.view.dock(self.)
        # here we got the view.

    # async def on_load(self) -> None:


HoverApp.run()
