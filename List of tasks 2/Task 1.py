import datetime
from random import choice


class Note:
    count_of_notes = 0

    def __init__(self, text, tag):
        Note.count_of_notes += 1
        self.text = text
        self.tag = tag
        self.date = datetime.date.today()
        self.ID = Note.count_of_notes

    def match(self, query):
        if query in self.text or query in self.tag:
            return True
        return False

    def __str__(self):
        return f"{self.ID}\n{self.date}\n{self.text}\n#{self.tag}\n"


class Notebook:
    def __init__(self):
        self.notes = list()

    def new_note(self, text, tag):
        self.notes.append(Note(text, tag))

    def modify_text(self, ID, new_text):
        for note in self.notes:
            if note.ID == ID:
                note.text = new_text
                break

    def modify_tag(self, ID, new_tag):
        for note in self.notes:
            if note.ID == ID:
                note.tag = new_tag
                break

    def search(self, query):
        found_notes = list()
        for note in self.notes:
            if note.match(query):
                found_notes.append(note)
        return found_notes


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def show_menu(self):
        for option_k, option_v in self.options.items():
            print(option_k, option_v.__name__)

    def run(self):
        while True:
            self.show_menu()
            choice = input("> ")
            correct_answers = ["1", "2", "3", "4", "5"]
            while choice not in correct_answers:
                print("Invalid input")
                choice = input("> ")

            self.options[choice]()

    def show_notes(self, notes = None):
        if notes is None:
            notes = self.notebook.notes
        if not notes:
            print("No notes found")
        for note in notes:
            print(note)

    def search_notes(self):
        query = input("Enter text which you want to find: ")
        notes = self.notebook.search(query)
        self.show_notes(notes)

    def add_note(self):
        text = input("Enter a text: ")
        tag = input("Enter a tag: ")
        self.notebook.new_note(text, tag)
        print("You added new note")

    def modify_note(self):
        what = -1
        ID = -1

        try:
            ID = int(input("Enter an ID of the note: "))
            what = int(input("What do you want to modify (1-text 2-tag): "))
        except ValueError:
            print("Input must be a number")
            self.modify_note()
            return

        if what not in [1, 2]:
            self.modify_note()
            return

        is_ID = False
        for note in self.notebook.notes:
            if ID == note.ID:
                is_ID = True
                break
        if not is_ID:
            print("The note wasn't found")
            self.modify_note()
            return

        if what == 1:
            new_text = input("Enter new text: ")
            self.notebook.modify_text(ID, new_text)
        elif what == 2:
            new_tag = input("Enter new tag: ")
            self.notebook.modify_tag(ID, new_tag)

    def quit(self):
            print("Bye")
            exit(0)

if __name__ == "__main__":
    menu = Menu()
    menu.run()