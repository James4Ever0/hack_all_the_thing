# https://github.com/sirfuzzalot/textual-inputs

from textual_inputs import TextInput
from textual.app import App

import os

keywords = set(["recursive"])
filepath = "./jq_man.log"

import textwrap
from ck_widgets_lv import ListViewUo


from textual.widgets import ScrollView

from textual.reactive import Reactive
from textual.widget import Widget
from rich.text import Text
from rich.panel import Panel

with open(filepath, "r") as f:
    content = f.read()


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


class MyApp(App):
    # how to let me copy the text inslde? fuck?
    index = 0
    readerName = "viewer"
    content_line_char_count = []
    lineNumbers = [2235]  # adjusted.
    # lineNumbers = [2268]
    # lineNumbers=[2923,2878,0,5] # we test this on android first.
    def wrapText(self, textList, width):  # the width is col-1
        content_line_char_count = []
        wrapped_lines = []
        for text in textList:
            lines = textwrap.wrap(text, width=width)
            lineCount = len(lines)
            if lineCount == 0:
                lines = [""]
                lineCount = 1
            content_line_char_count.append(lineCount)
            wrapped_lines.extend(lines)
        return wrapped_lines, content_line_char_count

    async def on_key(self, event):
        key = event.key
        key_lower = key.lower()
        if key_lower == "t":
            await self.mainToggle()
        elif key_lower == "j":
            await self.jumpScrollView()
        elif key_lower == "k":
            await self.jumpScrollView(reverse=True)
        elif key_lower == "s":
            await self.focusSearchView()
        elif key_lower == "a":
            await self.alterListView()

    async def mainToggle(self):  # you may need to adjust this thing?
        await self.view.action_toggle("side")
        await self.view.action_toggle("viewer")

    async def alterListView(self):
        if not self.scrollableHovers.visible:
            return
        import random

        label = random.randint(0, 10)
        # del self.view.named_widgets['side']
        # print(self.view.named_widgets)
        # print(self.view.named_widgets.keys())
        # breakpoint()
        del self.scrollableHovers
        # await self.remove(self.scrollableHovers)
        self.scrollableHovers = ListViewUo(
            [
                Hover(
                    "widget {}_{}".format(index, label),
                    onClick=lambda: self.mainToggle(),  # toggle what? jump to the viewer?
                )
                for index in range(30)
            ]
        )  # what should we update?
        await self.view.action_toggle("side")
        await self.view.dock(self.scrollableHovers, edge="top", name="side")  # WTF?
        # await self.view.action_toggle('side')

    async def action_clearSearchView(self):
        self.mainInput.value = ""

    async def focusSearchView(self):
        # await self.view.action_toggle('search')
        if not self.mainInput.visible:
            await self.view.action_toggle("search")
        await self.mainInput.focus()

    async def jumpScrollView(self, reverse: bool = False):
        if self.body.visible:
            self.index += -int(reverse)
            self.index %= len(self.lineNumbers)
            self.jumpToEquivalentLineNumber(
                self.content_line_char_count, self.lineNumbers[self.index]
            )

    # async def toggleScrollView(self):
    #     await self.view.action_toggle(self.readerName)

    async def on_load(self) -> None:
        await self.bind("enter", "submit", "Submit")
        await self.bind("ctrl+s", "searchToggle", "searchToggle")
        await self.bind("ctrl+u", "clearSearchView", "clearSearchView")
        await self.bind("escape", "reset_focus", show=False)

        from rich.text import Text

        size = os.get_terminal_size()
        columns, lines = size.columns, size.lines
        self.body = ScrollView(name=self.readerName)
        # self.height=lines-3
        textList = content.split("\n")
        wrapped_lines, self.content_line_char_count = self.wrapText(
            textList, columns - 1
        )
        processed_text = "\n".join(wrapped_lines)

        self.contentText = Text(processed_text)
        highlightLine = "will be efficient. In the example below the recursive call by _range to itself"
        highlightWord = "recursive"  # maybe not so right.
        self.contentText.highlight_words([highlightLine], style="black on red")
        self.contentText.highlight_words([highlightWord], style="yellow on red")

    async def on_mount(self) -> None:
        self.mainInput = TextInput(
            name="searchInput",
            placeholder="enter your query",
            title="lazero search",  # height = 3
        )
        await self.view.dock(self.mainInput, edge="top", size=3, name="search")
        await self.view.dock(
            self.body, edge="top", name="viewer"
        )  # remember that both 'body' and 'ListViewUo' are not visible at the start because there is nothing to display at this time.
        # when search is performed at the first time, 'ListViewUo' shows first.
        # search performed later depends on the visible component, if 'body' is visible then perform search inside this file, if 'ListViewUo' is visible then perform search across multiple files.
        await self.view.action_toggle("viewer")
        self.scrollableHovers = ListViewUo(
            [
                # this is bad. these things are not clickable.
                Hover("widget {}".format(index), onClick=lambda: self.mainToggle())
                for index in range(30)
            ]
        )

        # changes happens after hitting the enter key, if the search area is cleared, then do nothing.
        await self.view.dock(self.scrollableHovers, edge="top", name="side")

        await self.body.update(self.contentText)
        self.jumpToEquivalentLineNumber(
            self.content_line_char_count, self.lineNumbers[self.index]
        )

    def jumpToEquivalentLineNumber(self, content_line_char_count, lineNumber):
        size = os.get_terminal_size()
        equivalentLineCountPerLine = content_line_char_count

        lineNumber2 = sum(equivalentLineCountPerLine[:lineNumber])
        # lineNumber2 = max(0, lineNumber2-center)
        context = 4  # true context, no extra bullshit. -> real line on rendered result
        lineNumber2 = max(
            0, lineNumber2 - 1 - context
        )  # minus 1 to get the exact line location.
        self.body.set_y(lineNumber2)

    async def action_submit(self):
        value = self.mainInput.value
        if not value in ["", None]:
            # do something please?
            ...

    async def action_reset_focus(self):
        if self.body.visible:
            await self.body.focus()
            # add extra elif later
        else:
            await self.view.focus()

    async def action_searchToggle(self):
        await self.view.action_toggle("search")
        if self.mainInput.visible:
            await self.mainInput.focus()
        else:
            await self.view.focus()  # deactivate the search field?


MyApp.run(title="Lazero Viewer", log="textual.log")
