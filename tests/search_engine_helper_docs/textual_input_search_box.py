# aim to build some search box here. dock this.
# are you sure you will listen to the key events? let's try to toggle this thing via key 's', retrieve input via 'enter' key?

# make it centered.

# https://github.com/sirfuzzalot/textual-inputs

from textual_inputs import TextInput
from textual.app import App


class HoverApp(App):
    async def on_load(self) -> None:
        await self.bind("enter", "submit", "Submit")
        await self.bind('s','searchToggle', "searchToggle)
        # we want you to hide the thing!

    async def action_searchToggle(self):
        await self.view.action_toggle("search")


    async def action_submit(self):
        value = self.mainInput.value
        print("ENTERED VALUE: %s" % value)
        breakpoint()

    async def on_mount(self) -> None:
        self.mainInput = TextInput(name="query", placeholder="enter your query")
        await self.view.dock(self.mainInput, edge="top", name="search")


if __name__ == "__main__":
    HoverApp.run()
