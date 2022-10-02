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
        self.clickFunction = kwargs.pop("onClick", None)
        self.panelStyle = kwargs.pop("panelStyle", "")
        super().__init__(*args, **kwargs)

    def render(self) -> Panel:
        text = Text(self.name)
        import os

        size = os.get_terminal_size()
        width = size.columns - 1
        return Panel(
            # this style is strange. we should alter it in some way.
            text,
            style=self.panelStyle,
            height=4,
            width=width,  # better config it in some way.
        )  # this is arguable. maybe for mobile device this will be different?
        # calculate this height according to terminal width, and make sure it does not go lower than 3.

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    async def on_click(self):
        if self.clickFunction:
            await self.clickFunction()  # what should you pass?
            # assume to be some async function?
        # if self.name == "widget 1":
        #     # import os
        #     # command = 'bash less_jump_to_line.sh'
        #     # os.system(command) # does not work properly! fuck.
        # else:
        # print("CLICKED {}".format(self.name))
        # breakpoint()


class HoverApp(App):
    """Demonstrates custom widgets"""

    async def mainToggle(self):
        await self.view.action_toggle("side")
        await self.view.action_toggle("viewer")

    async def on_key(self, event):
        # self.console.bell()
        key = event.key
        # print("KEYCODE: {}".format(key)) # we want something like 'ESC'
        # breakpoint() # 'escape'
        # https://github.com/Textualize/textual/blob/e406458b8917d660197b8eeafcc1b7fde01e32a6/src/textual/keys.py
        key_lower = key.lower()
        # handle input elsewhere?
        # when text field is focused, we do not do shit.
        if key_lower in ["t"]:  # i doubt that 'escape' shall be treated differently.
            await self.mainToggle()
        elif key_lower == "a":
            await self.alterListView()

    async def alterListView(self):
        import random
        label = random.randint(0,10)
        self.scrollableHovers= ListViewUo([
            Hover("widget {}_{}".format(index, label), onClick=lambda: self.mainToggle())
            for index in range(30)
        ])  # what should we update?

    async def on_mount(self) -> None:
        # self.hovers = (
        #     Hover(
        #         "widget {}".format(index),
        #     )
        #     for index in range(3)
        # )
        self.mainViewer = ScrollView()  # with name or not? you need keywords.
        # hoverRenderable = self.hovers
        await self.mainViewer.update(
            Text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "
                * 20
            )
        )
        # self.renderableHovers = Table()
        self.scrollableHovers = ListViewUo(
            [
                # this is bad. these things are not clickable.
                Hover("widget {}".format(index), onClick=lambda: self.mainToggle())
                for index in range(30)
            ]
        )
        #     self.renderableHovers.add_row(
        #         Hover(
        #             "widget {}".format(index),
        #         )
        #     )

        await self.view.dock(self.scrollableHovers, edge="top", name="side")  # WTF?
        await self.view.dock(self.mainViewer, edge="top", name="viewer")
        await self.view.action_toggle("viewer")
        # here we got the view.

    # async def on_load(self) -> None:


HoverApp.run()
