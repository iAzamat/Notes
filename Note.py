import uuid
from datetime import datetime


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:3], title="текст", body="текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def to_file(note):
        return [note.id, note.title, note.body, note.date]

    def map_note(note):
        return '\n' \
               'ID: ' + note.id + '\n' + \
            'Заголовок: ' + note.title + '\n' + \
            'Тело: ' + note.body + '\n' + \
            'Дата публикации: ' + note.date
