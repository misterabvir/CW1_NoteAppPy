from Views.UI import UI
from Views.Commands.Command import Command


class CommandEdit(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "edit note"

    def execute(self) -> None:
        self.ui.edit()

    def info(self) -> str:
        return self.txt
