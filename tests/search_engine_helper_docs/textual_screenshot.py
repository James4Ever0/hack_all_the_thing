from textual.app import App
from rich.console import Console




class MyApp(App):
    async def on_load(self) -> None:
        await self.bind("y", "screenshot", "Screenshot")
    async def on_

    def action_screenshot(self) -> None:
        console = Console(record=True)
        console.print(self)
        console.export_text(clear=False) # so we can see the console afterwards.
        console.save_svg("screenshot.svg", title="MyTitle") # not so right?