from textual.app import App
from rich.console import Console


from textual.widgets import ScrollView


class MyApp(App):
    async def on_load(self) -> None:
        await self.bind("y", "screenshot", "Screenshot")
    async def on_mount(self):
        self.body = ScrollView()
        self.body.update(Text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'*200))
        await self.view.dock(self.body, edge="top")


    def action_screenshot(self) -> None:
        console = Console(record=True)
        console.print(self)
        console.export_text(clear=False) # so we can see the console afterwards.
        console.save_svg("screenshot.svg", title="MyTitle") # not so right?

MyApp.run()