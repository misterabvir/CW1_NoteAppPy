from Models.Keepers.JsonKeeper import JsonKeeper
from Models.Service import Service


class NoteController:
    def __init__(self):
        self.service = Service(JsonKeeper('data.json'))

    def show_all(self) -> str:
        return self.service.get_info()

    def add_note(self, title, content) -> bool:
        return self.service.add_note(title, content)

    def remove_note(self, note_id) -> bool:
        return self.service.remove(note_id)

    def edit_note(self, note_id, title, content):
        self.service.update(note_id, title, content)

    def save(self) -> bool:
        return self.service.save()
