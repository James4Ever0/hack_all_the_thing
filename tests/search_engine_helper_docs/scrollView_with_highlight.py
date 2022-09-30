lineNumber = 2268
# notice: this is the line.
#  'text': '       erator will be efficient. In the example below the recursive
# call by _range\n'
keywords = set(['recursive'])
filepath ='/root/Desktop/works/hack_all_the_thing/tests/search_engine_helper_docs/jq_man.log'

from textual.widgets import ScrollView
view = ScrollView()
content = with open(filepath, 'r') as f:
f.read()
view.update(content)
view.scroll_in_to_view(lineNumber)