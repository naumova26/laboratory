def greet(name):
    return f"Привет, {name}!"

print(greet("Анастасия"))

class Птицы:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} пшшш"

class Ворона(Птицы):
    def kar(self):
        return f"{self.name} курлык"

xomak = Птицы('хомяк')
print(xomak.speak())

vorona = Ворона('Птица')
print(vorona.speak())
print(vorona.kar())
