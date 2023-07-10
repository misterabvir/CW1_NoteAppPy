from Views.UI import UI
from Views.Commands.Command import Command


class CommandAdd(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "add new note"

    def execute(self) -> None:
        self.ui.add()

    def info(self) -> str:
        return self.txt
