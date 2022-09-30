lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'

# notice: terminal interface is not stable.

keywords = set(["recursive"])
filepath = (
    "/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log"
)
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

content_line_char_count = [len(line) for line in content.split("\n")]


class MyApp(App):
    # how to let me copy the text inslde? fuck?
    async def on_key(self, event):
        # self.console.bell()
        key = event.key
        if key == "c":
            await self.copyScrollView()

    async def jumpScrollView(self):
        # jump to next candidate.
        # will it work for hidden ScrollView
        await self.body

    async def copyScrollView(self):
        # results=self.body.__rich_repr__() # generator!
        # [('name','ScrollView#1')]
        await self.view.action_toggle("ScrollView#1")
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
        self.body = ScrollView()

        from rich.text import Text

        self.contentText = Text(content)
        highlightLine = "       erator will be efficient. In the example below the recursive call by _range\n"
        highlightWord = "recursive"  # maybe not so right.
        self.contentText.highlight_words([highlightLine], style="black on red")
        self.contentText.highlight_words([highlightWord], style="yellow on red")
        # await self.bind('c',action,'Copy')

    async def on_mount(self) -> None:
        # self.set_interval(5, self.refresh)
        await self.view.dock(self.body, edge="top")
        await self.body.update(self.contentText)
        import os

        size = os.get_terminal_size()
        # msize = self.body.window.layout.width# it is totally not right!
        # the width is zero. means adaptive?
        # print("WINDOW SIZE:", msize) # not right!
        columns, lines = size.columns, size.lines
        # print("COLUMNS:", columns)
        # center = int(lines/2)
        # breakpoint()
        import math

        equivalentLineCountPerLine = [
            max(
                1, math.ceil(length / (columns - 1))
            )  # that's because of the scrollbar taking 1 extra column.
            for length in content_line_char_count
        ]

        lineNumber2 = sum(equivalentLineCountPerLine[:lineNumber])
        # lineNumber2 = max(0, lineNumber2-center)
        context = 1
        lineNumber2 = max(
            0, lineNumber2 - 1 - context
        )  # minus 1 to get the exact line location.
        # you want more context?
        # total_sum =
        # print("TOTAL_SUM:", sum(equivalentLineCountPerLine))
        # print("LINE TOTAL COUNT:", len(content_line_char_count))
        # # breakpoint()
        # print("LINE NUMBER:", lineNumber)
        # print("LINE NUMBER 2:", lineNumber2)
        # breakpoint()
        self.body.set_y(lineNumber2)


MyApp.run(title="Code Viewer", log="textual.log")
