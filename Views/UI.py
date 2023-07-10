from __future__ import annotations
from abc import ABC, abstractmethod

class UI(ABC):
    @abstractmethod
    def start_ui(self) -> None:
        '''Старт представления'''
        pass

    @abstractmethod
    def show(self) -> None:
        '''Показать заметки'''
        pass

    @abstractmethod
    def add(self) -> None:
        '''Добавить заметку'''
        pass

    @abstractmethod
    def remove(self) -> None:
        '''Удалить заметку'''
        pass

    @abstractmethod
    def save(self) -> None:
        '''Сохранить заметку'''
        pass

    @abstractmethod
    def edit(self) -> None:
        '''Редактировать заметку'''
        pass

    @abstractmethod
    def quit(self) -> None:
        '''Выйти из приложения'''
        pass