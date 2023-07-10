from Views.UI import UI
from Views.Commands.Command import Command


class CommandRemove(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "remove note"

    def execute(self) -> None:
        self.ui.remove()

    def info(self) -> str:
        return self.txt
