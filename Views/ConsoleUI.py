import os
import sys

from Controllers.NoteController import NoteController
from Views.Menu import Menu
from Views.UI import UI

INPUT_FIELD = "> " 
'''Поле ввода'''

INPUT_WRONG = "Wrong input, try again"
'''Сообщение о неверном вводе'''

ENTER_MENU = "Enter the menu item"
'''Сообщение о выборе пункта меню'''

ENTER_ID = "Enter the note id"
'''Сообщение о вводе id заметки'''

ENTER_TITLE = "Enter the title"
'''Сообщение о вводе наименования заметки'''

ENTER_CONTENT = "Enter the content"
'''Сообщение о вводе содержимого заметки'''

DONE = "Done!"
'''Сообщение о положительном результате'''



def get_int_input(message: str, minimum: int, maximum: int = sys.maxsize) -> int:
    '''
        Получение ввода целочисленного числа в заданном диапазоне пользователя.
        -----       
        Параметры:
            message (str): Сообщение для пользователя\n
            minimum (int): Значение минимального диапазона\n
            maximum (int): Значение максимального диапазона\n
    '''
    print(message)
    choice = input(INPUT_FIELD)
    while not str(choice).isdigit() or not (minimum <= int(choice) <= maximum):
        print(INPUT_WRONG)
        choice = input(INPUT_FIELD)
    return int(choice)


def get_str_not_empty_input(message: str) -> str:
    """
        Получение строкового (не пустого) ввода.
        ------       
        Параметры:
            message (str): Сообщение для пользователя\n
    """
    print(message)
    choice = input(INPUT_FIELD)
    while choice == "":
        print(INPUT_WRONG)
        choice = input(INPUT_FIELD)
    return choice


class ConsoleUI(UI):
    """Реализация класса представления для консоли

    Args:
        UI (_type_): Базовый класс представления
    """

    def __init__(self) -> None: 
        self.isWork = True
        self.menu = Menu(self)
        self.title = "NOTES"
        self.controller = NoteController()

    def start_ui(self) -> None:
        print(self.title)
        print(self.menu.draw())
        while self.isWork:
            choice = get_int_input(ENTER_MENU, 1, self.menu.get_size()) - 1
            os.system('CLS')
            print(self.title)
            print(self.menu.draw())
            self.menu.execute(choice)

    def show(self) -> None:
        print(self.controller.show_all())

    def add(self) -> None:
        title = get_str_not_empty_input(ENTER_TITLE)
        content = get_str_not_empty_input(ENTER_CONTENT)
        if self.controller.add_note(title, content):
            print(DONE)

    def remove(self) -> None:
        note_id = get_int_input(ENTER_ID, 0)
        if self.controller.remove_note(note_id):
            print(DONE)

    def save(self) -> None:
        if self.controller.save():
            print(DONE)

    def edit(self) -> None:
        note_id = get_int_input(ENTER_ID, 0)
        title = get_str_not_empty_input(ENTER_TITLE)
        content = get_str_not_empty_input(ENTER_CONTENT)
        self.controller.edit_note(note_id, title, content)

    def quit(self) -> None:
        self.isWork = False
