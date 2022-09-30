lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'
keywords = set(['recursive'])
filepath ='/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log'
# are you sure this will really jump to the freaking line???

from textual.widgets import ScrollView
from textual.scrollbar import ScrollTo

from textual.app import App

class MyApp(App):
    # how to let me copy the text inslde? fuck?
    async def on_load(self) -> None:
        self.body = ScrollView()
        with open(filepath, 'r') as f:
            content = f.read()
        from rich.text import Text
        self.contentText = Text(content)
        highlightLine = '       erator will be efficient. In the example below the recursive call by _range\n'
        highlightWord= 'recursive' # maybe not so right.
        self.contentText.highlight_words([highlightLine], style='black on red')
        self.contentText.highlight_words([highlightWord], style='aqua on red')

    async def on_mount(self) -> None:
        await self.view.dock(self.body, edge="top")
        await self.body.update(self.contentText)
        # self.body.y= lineNumber
        # self.body.target_y = lineNumber
        # self.body.animate("y", lineNumber, speed=lineNumber*3, easing="out_cubic")
        # self.body.set_y(lineNumber)
        # await self.body.watch_y(lineNumber)

        # self.body.scroll_in_to_view(lineNumber)
        # self.body.target_y = lineNumber
        # self.body.y = lineNumber
    
MyApp.run(title="Code Viewer", log="textual.log")
