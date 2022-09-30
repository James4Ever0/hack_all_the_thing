lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'
from rich.console import Console
keywords = set(['recursive'])
filepath ='/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log'
# are you sure this will really jump to the freaking line???

# you cannot select this thing. better use 'less'

from textual.widgets import ScrollView

from textual.app import App

class MyApp(App):
    # how to let me copy the text inslde? fuck?
    def on_key(self, event):
        # self.console.bell()
        key = event.key
        if key == 'c':
            self.copyScrollView()
    def copyScrollView(self):
        console= Console()
        #nothing!
        # self.body.console.begin_capture() # [(text, style, control), ...]
        # nothing here?
        with self.console.capture() as capture:
            # self.body.window.layout.render(console)
        #     console.print(self.body.window.layout.render(console))
        # result = capture.get()

        print("RESULT:", result)
        breakpoint()
    async def on_load(self) -> None:
        # action = 'copyScrollView()'
        self.body = ScrollView()
        with open(filepath, 'r') as f:
            content = f.read()
        from rich.text import Text
        self.contentText = Text(content)
        highlightLine = '       erator will be efficient. In the example below the recursive call by _range\n'
        highlightWord= 'recursive' # maybe not so right.
        self.contentText.highlight_words([highlightLine], style='black on red')
        self.contentText.highlight_words([highlightWord], style='yellow on red')
        # await self.bind('c',action,'Copy')

    async def on_mount(self) -> None:
        # self.set_interval(5, self.refresh)
        await self.view.dock(self.body, edge="top")
        await self.body.update(self.contentText)
        # self.body.y= lineNumber
        # self.body.target_y = lineNumber
        # scrollTo = ScrollTo(self.body.vscroll, 0, lineNumber)
        # await self.body.emit(scrollTo)
        self.body.set_y(lineNumber)
        # with self.body.window.console.capture() as capture:
        #     self.body.window.
        # result = capture.get()
        # mRich = self.body.__rich__() # wtf?

        # self.body.animate("y", lineNumber,speed=lineNumber*3, easing="out_cubic")
        # await self.body.watch_y(lineNumber)

        # self.body.scroll_in_to_view(lineNumber)
        # self.body.target_y = lineNumber
        # self.body.y = lineNumber
    
MyApp.run(title="Code Viewer", log="textual.log")
