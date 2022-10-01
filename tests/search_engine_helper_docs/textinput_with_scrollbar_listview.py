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
            name="search",
            placeholder="enter your query",
            title="search input",  # height = 3
        )
        await self.view.dock(self.mainInput, edge="top", size=3)
        await self.view.dock(self.body, edge="top")

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

    async def action_reset_focus(self):
        await self.view.focus()

    async def action_searchToggle(self):
        await self.view.action_toggle("search")
        if self.mainInput.visible:
            await self.mainInput.focus()
        else:
            await self.view.focus()  # deactivate the search field?


MyApp.run(title="Code Viewer", log="textual.log")
