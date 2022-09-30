lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'
keywords = set(['recursive'])
filepath ='/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log'
# are you sure this will really jump to the freaking line???

from textual.widgets import ScrollView
view = ScrollView()
with open(filepath, 'r') as f:
    content = f.read()
from rich.text import Text
contentText = Text(content)

from textual.app import App

class MyApp(App):
    # how to let me copy the text inslde? fuck?
    async def on_mount(self) -> None:
        await self.view.dock(view, edge="top")
        await view.update(contentText)
        view.scroll_in_to_view(lineNumber)
    
MyApp.run(title="Code Viewer", log="textual.log")
