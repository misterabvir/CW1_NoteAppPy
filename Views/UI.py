from __future__ import annotations
from abc import ABC, abstractmethod


class UI(ABC):
    @abstractmethod
    def start_ui(self) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def add(self) -> None:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def edit(self) -> None:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass
