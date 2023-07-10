from Models.Keepers.Keeper import Keeper
from Models.NoteModels.Notes import Notes


class Service:
    def __init__(self, keeper: Keeper) -> None:
        self.keeper = keeper
        self.notes: Notes = self.get_notes()

    def get_notes(self) -> Notes:
        load = self.keeper.load()
        if len(load) > 0:
            return Notes().parse_list(load)
        else:
            return Notes()

    def save(self) -> bool:
        return self.keeper.save(self.notes.get_list())

    def add_note(self, title, content) -> bool:
        return self.notes.add_note(title, content)

    def remove(self, note_id: int) -> bool:
        return self.notes.remove(note_id)

    def update(self, note_id, title, content) -> None:
        self.update(note_id, title, content)

    def get_detail(self, note_id) -> str:
        return self.notes.get_detail(note_id)

    def get_info(self) -> str:
        return self.notes.get_info()
