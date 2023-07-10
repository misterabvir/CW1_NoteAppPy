from datetime import datetime


class Note:
    def __init__(self, note_id: int, title: str, content: str) -> None:
        self.note_id: int = note_id
        self.title: str = title
        self.content: str = content
        self.date: str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def __str__(self):
        output = "[#" + str(self.note_id) + "]. "
        output += self.title.upper() + "\n\r"
        output += "[" + self.date + "]\n\r"
        output += self.content + "\n\r"
        return output

    def get_id(self) -> int:
        return self.note_id

    def get_dict(self) -> dict:
        return {"note_id": self.note_id, "title": self.title, "content": self.content, "date": self.date}

    def parse_dict(self, dictionary: dict):
        self.note_id = dictionary["note_id"]
        self.title = dictionary["title"]
        self.content = dictionary["content"]
        self.date = dictionary["date"]
        return self

    def get_info(self) -> str:
        return f'[#{self.note_id}] {self.title}\n{self.date}\n{self.content}'
