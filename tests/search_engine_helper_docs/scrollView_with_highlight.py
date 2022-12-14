# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'
# notice: terminal interface is not stable.
import os

keywords = set(["recursive"])
filepath = "./jq_man.log"

# implement soft/hard wrap method yourself, or the scroll view will get tricky.
import textwrap


# filepath = "test.txt"  # col: 108
# now check the layout?
# col=10 -> 9
# col=1 -> 0
# end digit: 7 -> 108
# there is no scrollbar. fuck.
# with scrollbar: width=1. end digit: 6 -> 107
# minus 2?
# cat: col=108 -> 7
# are you sure this will really jump to the freaking line???
# from rich.console import Console

# you cannot select this thing. better use 'less'

from textual.widgets import ScrollView

from textual.app import App

with open(filepath, "r") as f:
    content = f.read()

# content_line_char_count = [len(line) for line in content.split("\n")]
# get it from somewhere else.
# better store it in self.content_line_char_count


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
        # self.console.bell()
        key = event.key
        if key == "t":
            await self.toggleScrollView()
        elif key == "j":
            await self.jumpScrollView()

    async def jumpScrollView(self):
        # jump to next candidate.
        # will it work for hidden ScrollView
        if self.body.visible:
            self.index += 1
            self.index %= len(self.lineNumbers)
            self.jumpToEquivalentLineNumber(
                self.content_line_char_count, self.lineNumbers[self.index]
            )

    async def toggleScrollView(self):
        # results=self.body.__rich_repr__() # generator!
        # [('name','ScrollView#1')]
        await self.view.action_toggle(self.readerName)
        # print("toggle code review")
        # print("disable mouse capture")
        # not able to disable this shit at all.

        # disable mouse capture instead.
        # console = Console()
        # with console.capture() as capture:
        #     self.body.window.render_lines()
        #     result2= self.body.window.render_cache
        #     # result2 = self.body.window.refresh(repaint=True) # renderable!
        # result = capture.get()
        # # results_list = [x for x in results]

        # print("RESULT:", [result], type(result))
        # print("RESULT2:", [text[0] for text in result2.lines])
        # breakpoint()

    async def on_load(self) -> None:
        # action = 'copyScrollView()'
        self.body = ScrollView(name=self.readerName)

        from rich.text import Text

        size = os.get_terminal_size()
        columns, lines = size.columns, size.lines
        textList = content.split("\n")
        wrapped_lines, self.content_line_char_count = self.wrapText(
            textList, columns - 1
        )
        processed_text = "\n".join(wrapped_lines)

        self.contentText = Text(processed_text)
        # highlightLine = "       erator will be efficient. In the example below the recursive call by _range\n"
        highlightLine = "will be efficient. In the example below the recursive call by _range to itself"
        highlightWord = "recursive"  # maybe not so right.
        self.contentText.highlight_words([highlightLine], style="black on red")
        self.contentText.highlight_words([highlightWord], style="yellow on red")
        # await self.bind('c',action,'Copy')

    async def on_mount(self) -> None:
        # self.set_interval(5, self.refresh)
        await self.view.dock(self.body, edge="top")

        # register something on window size change?

        await self.body.update(self.contentText)
        self.jumpToEquivalentLineNumber(
            self.content_line_char_count, self.lineNumbers[self.index]
        )

    def jumpToEquivalentLineNumber(self, content_line_char_count, lineNumber):
        size = os.get_terminal_size()
        # msize = self.body.window.layout.width# it is totally not right!
        # the width is zero. means adaptive?
        # print("WINDOW SIZE:", msize) # not right!
        # columns, lines = size.columns, size.lines
        # print("COLUMNS:", columns)
        # center = int(lines/2)
        # breakpoint()
        equivalentLineCountPerLine = content_line_char_count

        # equivalentLineCountPerLine = [
        #     max(
        # #         1, math.ceil(length / (columns-1))
        #         1, math.ceil(length)
        #     )  # that's because of the scrollbar taking 1 extra column.
        #     for length in content_line_char_count
        # ]

        lineNumber2 = sum(equivalentLineCountPerLine[:lineNumber])
        # lineNumber2 = max(0, lineNumber2-center)
        context = 4  # true context, no extra bullshit. -> real line on rendered result
        lineNumber2 = max(
            0, lineNumber2 - 1 - context
        )  # minus 1 to get the exact line location.

        # print("LINE NUMBER:", lineNumber)
        # print("LINE NUMBER 2:", lineNumber2)
        # print("LEN:", len(equivalentLineCountPerLine))
        # breakpoint()
        # self.body.set_y(lineNumber2)
        self.body.set_y(lineNumber2)  # how about let's not alter this thing?


MyApp.run(title="Code Viewer", log="textual.log")
