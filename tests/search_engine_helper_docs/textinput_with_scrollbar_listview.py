# https://github.com/sirfuzzalot/textual-inputs

from textual_inputs import TextInput
from textual.app import App

import os

keywords = set(["recursive"])
filepath = "./jq_man.log"

import textwrap


from textual.widgets import ScrollView

from textual.app import App

with open(filepath, "r") as f:
    content = f.read()


class MyApp(App):
    # how to let me copy the text inslde? fuck?
    index = 0
    readerName = "ScrollFileReader"
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
        if key == "t":
            await self.toggleScrollView()
        elif key == "j":
            await self.jumpScrollView()
        elif key == "s":
            await self.focusSearchView()

    async def action_clearSearchView(self):
        self.mainInput.value = ""

    async def focusSearchView(self):
        # await self.view.action_toggle('search')
        if not self.mainInput.visible:
            await self.view.action_toggle("search")
        await self.mainInput.focus()

    async def jumpScrollView(self):
        if self.body.visible:
            self.index += 1
            self.index %= len(self.lineNumbers)
            self.jumpToEquivalentLineNumber(
                self.content_line_char_count, self.lineNumbers[self.index]
            )

    async def toggleScrollView(self):
        await self.view.action_toggle(self.readerName)

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
            self.body, edge="top"
        )  # remember that both 'body' and 'ListViewUo' are not visible at the start because there is nothing to display at this time.
        # when search is performed at the first time, 'ListViewUo' shows first.
        # search performed later depends on the visible component, if 'body' is visible then perform search inside this file, if 'ListViewUo' is visible then perform search across multiple files.
        # changes happens after hitting the enter key, if the search area is cleared, then do nothing.
        await self.view.dock(self.scrollableHovers)

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
