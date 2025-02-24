class room():
    def __init__(self, number, kind, availability):
        self.numer = number
        self.kind = kind
        self.availability = True

    def book_room(self):
        if self.availability:
            self.availability = False
            return True
        return False
    
    def cancel_room(self):
        if not self.availability:
            self.availability = True
            return True
        return False


class Client():
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail