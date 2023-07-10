from __future__ import annotations

from abc import ABC, abstractmethod


class Keeper(ABC):
    @abstractmethod
    def save(self, obj) -> bool:
        pass

    @abstractmethod
    def load(self):
        pass
