# import rich

# let's check if we can have some bounding boxes.
from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.text import Text

panel_group = Group(
    Panel("Hello", style="on blue"),
    Panel(Text("World", style='yellow'), style="black on red"),
)
print(Panel(panel_group))
# it is a panel.

# we need textual. another library to make console interface.
# cause we are searching!