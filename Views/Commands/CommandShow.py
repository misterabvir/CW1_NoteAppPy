from Views.UI import UI
from Views.Commands.Command import Command


class CommandShow(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "Show notes"

    def execute(self) -> None:
        self.ui.show()

    def info(self) -> str:
        return self.txt
