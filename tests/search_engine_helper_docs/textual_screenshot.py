from textual.app import App
from rich.console import Console

class MyApp(App):
    async def on_load(self) -> None:
        await self.bind("y", "screenshot", "Screenshot")

    def action_screenshot(self) -> None:
        console = Console(record=True)
        console.print(self)
        console.save_svg("screenshot.svg", title="MyTitle")