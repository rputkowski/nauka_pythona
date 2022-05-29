# najprostszy sposób definiowania obiektu
# pass jest to miejsce dla funkcjonalności, która będzie dodana później
# pass może być użyte w ciele metody (a body),które nic nie robi
# def odejmij(a,b):
#   pass
# self reprezentuje instancję klasę. dzięki użyciu self my możemy mieć dostęp do właściwości i metod klasy w Pythonie
# Tworzenie obiektu realizujemy przez tzw. konstruktor - jest to specjalna metoda, która jest wykonywana kiedy tworzymy nasz obiekt.
class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")

    def info(self):
        print(f"Kolor obiektu to: {self.kolor_obiektu}")

    def info_ex(self, nazwa):
        print(f"Kolor obiektu {nazwa} to: {self.kolor_obiektu}")
# tworzymy obiekt na podstawie klasy, podajemy nazwę obiektu (paletka_a) i wywołujemy konstruktor klasy (Paletka())
# f-string
# val = 'Python course'
# print(f"Rezultat zwracany przez naszą zmienną to {val}")
# name = 'Rafal'
# age = 43
# print(f"Hello my name is {name} and I am {age} years old")
def testklasy():
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("*****************************************************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_a))
    print("*****************************************************************")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_b))
    print("*****************************************************************")
    print(f"Kolor dla paletka_a: {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b: {paletka_b.kolor_obiektu}")
    paletka_a.info()
    paletka_b.info()
    paletka_a.info_ex("a")
    paletka_b.info_ex("b")
