lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'

# notice: terminal interface is not stable.

keywords = set(["recursive"])
filepath = (
    "/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log"
)
# are you sure this will really jump to the freaking line???
# from rich.console import Console

# you cannot select this thing. better use 'less'

from textual.widgets import ScrollView

from textual.app import App



class MyApp(App):
    # how to let me copy the text inslde? fuck?
    async def on_key(self, event):
        # self.console.bell()
        key = event.key
        if key == "c":
            await self.copyScrollView()

    async def copyScrollView(self):
        # results=self.body.__rich_repr__() # generator!
        # [('name','ScrollView#1')]
        print("disable mouse capture")
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
        with open(filepath, "r") as f:
            content = f.read()
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
        self.body.set_y(lineNumber)


MyApp.run(title="Code Viewer", log="textual.log")
