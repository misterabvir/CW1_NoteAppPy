from Views.UI import UI
from Views.Commands.Command import Command


class CommandQuit(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "quit"

    def execute(self) -> None:
        self.ui.quit()

    def info(self) -> str:
        return self.txt
