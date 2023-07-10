from Views.UI import UI
from Views.Commands.Command import Command


class CommandSave(Command):

    def __init__(self, ui: UI):
        self.ui = ui
        self.txt = "save"

    def execute(self) -> None:
        self.ui.save()

    def info(self) -> str:
        return self.txt
