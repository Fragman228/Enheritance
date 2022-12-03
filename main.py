class Hero:
    def __init__(self, name, health, armour, attac):
        self.name = name
        self.health = health
        self.armour = armour
        self.attac = attac
    def print_info(self):
        print(f"Уровень здоровья - {self.health}")
        print(f"Класс брони - {self.armour}\n")
class Magician(Hero):
    def hello(self):
        print(f"Поприветствуйте война {self.name}")
    def attack(self, enemy):
        print(f"Маг аттакует противника {enemy} и наносит ему урон {self.attac}")

