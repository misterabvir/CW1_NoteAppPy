from Models.NoteModels.Note import Note


class Notes:
    def __init__(self, data=None):
        self.notes: list[Note] = []
        if data is not None:
            self.parse_list(data)

    def get_size(self) -> int:
        return len(self.notes)

    def get_info(self) -> str:
        output = ''
        for item in self.notes:
            output += item.get_info()
        return output

    def get_detail(self, note_id: int) -> str:
        for item in self.notes:
            if item.get_id() == note_id:
                return item.get_info()
        return "not found"

    def add_note(self, header: str, content: str) -> bool:
        index = self.get_index()
        note = Note(index, title=header, content=content)
        self.notes.append(note)
        return True

    def update(self, note_id: int, header: str, content: str) -> None:
        self.remove(note_id)
        note = Note(note_id, title=header, content=content)
        self.notes.append(note)

    def remove(self, note_id: int) -> bool:
        for item in self.notes:
            if item.get_id() == note_id:
                self.notes.remove(item)
                return True
        return False

    def get_index(self):
        if len(self.notes) == 0:
            return 0
        max_index = 0
        for item in self.notes:
            if max_index <= item.get_id():
                max_index = item.get_id() + 1
        return max_index

    def get_list(self) -> list:
        note_list = []
        for note in self.notes:
            note_list.append(note.get_dict())
        return note_list

    def parse_list(self, note_list: list):
        self.notes = []
        for item in note_list:
            note = Note(0, '', '').parse_dict(item)
            self.notes.append(note)
        return self
