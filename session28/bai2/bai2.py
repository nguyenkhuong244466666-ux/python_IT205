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
            return self.__base_hp + other.__base_hp
        return 0


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

    def __init__(self, hp, strength):
        super().__init__(hp, strength)

    def attack_enemy(self):
        damage_warrior = Warrior.attack_enemy(self)
        damage_magic = MagicalStance.attack_enemy(self)
        return damage_warrior + damage_magic


class VolcanoZone:

    def activate_buff(self, character):
        print(f"Volcano buff cho {character.__class__.__name__}")


def apply_battleground_effect(environment, character):
    environment.activate_buff(character)


current_hero = None


def show_menu():
    print("\n===== RPG SYSTEM =====")
    print("1. Tao nhan vat")
    print("2. Danh quai")
    print("0. Thoat")


def main():

    global current_hero

    while True:

        show_menu()

        choice = input("Chon: ")

        match choice:

            case "1":

                try:
                    hp = int(input("Nhap HP: "))
                    strength = int(input("Nhap Strength: "))

                    current_hero = Spellblade(hp, strength)

                    total_hp = current_hero + current_hero

                    print(f"Tao Spellblade thanh cong | HP: {current_hero.base_hp} | Strength: {current_hero.strength} | Tong HP: {total_hp}")

                    print(f"MRO: {Spellblade.__mro__}")
                except:
                    print("Du lieu khong hop le")
            case "2":

                if current_hero is None:

                    print("Chua co nhan vat")

                else:

                    damage = current_hero.attack_enemy()

                    print(f"Sat thuong gay ra: {damage}")

                    zone = VolcanoZone()

                    apply_battleground_effect(zone, current_hero)

            case "0":

                print("Da thoat")

                break
            case _:

                print("Sai lua chon")

main()