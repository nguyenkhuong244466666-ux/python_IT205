from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, hp):
        self.__base_hp = hp

    @property
    def base_hp(self):
        return self.__base_hp

    @abstractmethod
    def attack_enemy(self):
        pass

    def __add__(self, other):
        if isinstance(other, BaseCharacter):
            return int(self.__base_hp + other.__base_hp)
        return NotImplemented


class Warrior(BaseCharacter):
    def __init__(self, hp, strength):
        super().__init__(hp)
        self.strength = strength

    def attack_enemy(self):
        return self.strength * 2.5


class MagicalStance:
    def attack_enemy(self):
        return 150.0


class Spellblade(Warrior, MagicalStance):
    def attack_enemy(self):
        return Warrior.attack_enemy(self) + MagicalStance.attack_enemy(self)


class VolcanoZone:
    def activate_buff(self, character):
        print("Volcano Zone kích hoạt buff")
        return character.attack_enemy() + 50


def apply_battleground_effect(environment, character):
    return environment.activate_buff(character)


current_hero = None

while True:
    print("\n===== RPG SYSTEM =====")
    print("1. Khởi tạo Ma kiếm sĩ")
    print("2. Giao tranh")
    print("3. Thoát")

    choice = input("Chọn chức năng: ")

    match choice:
        case "1":
            hp = int(input("Nhập HP: "))
            strength = int(input("Nhập Strength: "))

            current_hero = Spellblade(hp, strength)

            print("Khởi tạo thành công!")
            print("Tổng HP tích lũy:", current_hero + current_hero)

        case "2":
            if current_hero is None:
                print("Chưa khởi tạo nhân vật!")
            else:
                print("Sát thương tổng hợp:", current_hero.attack_enemy())

                volcano = VolcanoZone()
                print("Sát thương sau buff:", apply_battleground_effect(volcano, current_hero))

        case "3":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")