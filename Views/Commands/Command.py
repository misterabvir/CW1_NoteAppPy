from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        """
        action execute, pattern Command
        :return:
        """
        pass

    @abstractmethod
    def info(self) -> str:
        """
        string presentation of action
        :return:
        """
        pass
