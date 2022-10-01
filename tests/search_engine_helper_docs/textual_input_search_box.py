# aim to build some search box here. dock this.
# are you sure you will listen to the key events? let's try to toggle this thing via key 's', retrieve input via 'enter' key?

# make it centered.

# https://github.com/sirfuzzalot/textual-inputs

from textual_inputs import TextInput
from textual.app import App

class HoverApp(App):
    mainInput=None
    async def on_load(self) -> None:
        await self.bind("enter", "submit", "Submit")
    async def action_submit(self):
        value = self.mainInput.value
        print("ENTERED VALUE: %s" % value)
        breakpoint()
    async def on_mount(self) -> None: