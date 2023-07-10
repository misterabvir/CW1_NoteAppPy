from Views.Commands.CommandShow import CommandShow
from Views.Commands.CommandAdd import CommandAdd
from Views.Commands.CommandRemove import CommandRemove
from Views.Commands.CommandEdit import CommandEdit
from Views.Commands.CommandSave import CommandSave
from Views.Commands.CommandQuit import CommandQuit
from Views.UI import UI


class Menu:
    def __init__(self, ui: UI) -> None:
        self.commands = []
        self.commands.append(CommandShow(ui))
        self.commands.append(CommandAdd(ui))
        self.commands.append(CommandRemove(ui))
        self.commands.append(CommandEdit(ui))
        self.commands.append(CommandSave(ui))
        self.commands.append(CommandQuit(ui))

    def draw(self) -> str:
        output = ""
        index = 1
        for item in self.commands:
            output += str(index) + ". " + item.info() + "\r\n"
            index += 1
        return output

    def execute(self, choice: int):
        self.commands[choice].execute()

    def get_size(self) -> int:
        return len(self.commands)
