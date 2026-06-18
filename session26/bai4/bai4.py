from abc import ABC, abstractmethod


class Equipment(ABC):
    """
    Lớp trừu tượng cho mọi loại trang bị.
    """

    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    """
    Vũ khí vật lý.
    """

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return False

        return (
            self.calculate_total_damage()
            > other.calculate_total_damage()
        )

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return self

        new_name = (
            f"Fusion({self.name} + {other.name})"
        )

        new_base_damage = (
            self.base_damage + other.base_damage
        )

        new_upgrade_level = (
            self.upgrade_level
            + other.upgrade_level
        )

        return Weapon(
            new_name,
            new_base_damage,
            new_upgrade_level
        )


class MagicMixin:
    """
    Thuộc tính phép thuật.
    """

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(
            f"{self.name} đang phát sáng ma thuật!"
        )


class MagicSword(Weapon, MagicMixin):
    """
    Kiếm ma thuật.
    """

    def __init__(
        self,
        name,
        base_damage,
        upgrade_level,
        magic_power
    ):
        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level
        )

        MagicMixin.__init__(
            self,
            magic_power
        )

    def calculate_total_damage(self):
        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


inventory = []


def show_inventory():

    print(
        "\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---"
    )

    if not inventory:
        print(
            "Kho vũ khí hiện đang trống."
        )

        print(
            "Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3."
        )

        return

    print(
        f"{'STT':<6}"
        f"{'Tên vũ khí':<30}"
        f"{'Loại':<15}"
        f"{'Cấp':<8}"
        f"{'Sát thương tổng'}"
    )

    print("-" * 80)

    for index, item in enumerate(
        inventory,
        start=1
    ):

        weapon_type = (
            type(item).__name__
        )

        print(
            f"{index:<6}"
            f"{item.name:<30}"
            f"{weapon_type:<15}"
            f"{item.upgrade_level:<8}"
            f"{item.calculate_total_damage()}"
        )


def forge_weapon():

    print(
        "\n--- RÈN VŨ KHÍ VẬT LÝ ---"
    )

    name = input(
        "Nhập tên vũ khí: "
    )

    try:
        base_damage = int(
            input(
                "Nhập sát thương gốc: "
            )
        )

        if base_damage <= 0:
            print(
                "Giá trị phải lớn hơn 0!"
            )
            return

        upgrade_level = int(
            input(
                "Nhập cấp cường hóa: "
            )
        )

        if upgrade_level <= 0:
            print(
                "Giá trị phải lớn hơn 0!"
            )
            return

    except ValueError:
        print(
            "Dữ liệu không hợp lệ!"
        )
        return

    weapon = Weapon(
        name,
        base_damage,
        upgrade_level
    )

    inventory.append(weapon)

    print(
        "\n>> Rèn vũ khí vật lý thành công!"
    )

    print(
        f"Tên vũ khí: {weapon.name}"
    )

    print("Loại: Weapon")

    print(
        f"Cấp cường hóa: {weapon.upgrade_level}"
    )

    print(
        f"Sát thương tổng: {weapon.calculate_total_damage()}"
    )


def forge_magic_sword():

    print(
        "\n--- RÈN KIẾM MA THUẬT ---"
    )

    name = input(
        "Nhập tên kiếm ma thuật: "
    )

    try:
        base_damage = int(
            input(
                "Nhập sát thương gốc: "
            )
        )

        if base_damage <= 0:
            print(
                "Giá trị phải lớn hơn 0!"
            )
            return

        upgrade_level = int(
            input(
                "Nhập cấp cường hóa: "
            )
        )

        if upgrade_level <= 0:
            print(
                "Giá trị phải lớn hơn 0!"
            )
            return

        magic_power = int(
            input(
                "Nhập sức mạnh phép thuật: "
            )
        )

        if magic_power <= 0:
            print(
                "Giá trị phải lớn hơn 0!"
            )
            return

    except ValueError:
        print(
            "Dữ liệu không hợp lệ!"
        )
        return

    sword = MagicSword(
        name,
        base_damage,
        upgrade_level,
        magic_power
    )

    inventory.append(sword)

    print(
        "\n>> Rèn kiếm ma thuật thành công!"
    )

    print(
        f"Tên vũ khí: {sword.name}"
    )

    print(
        "Loại: MagicSword"
    )

    print(
        f"Cấp cường hóa: {sword.upgrade_level}"
    )

    print(
        f"Sát thương gốc: {sword.base_damage}"
    )

    print(
        f"Sức mạnh phép thuật: {sword.magic_power}"
    )

    print(
        f"Sát thương tổng: {sword.calculate_total_damage()}"
    )


def compare_weapons():

    print(
        "\n--- THẨM ĐỊNH VŨ KHÍ ---"
    )

    if len(inventory) < 2:

        print(
            "Cần ít nhất 2 vũ khí trong kho để thẩm định!"
        )

        return

    weapon1 = inventory[0]
    weapon2 = inventory[1]

    print(
        f"Vũ khí thứ nhất:\n{weapon1.name} | Loại: {type(weapon1).__name__} | Sát thương: {weapon1.calculate_total_damage()}"
    )

    print(
        f"\nVũ khí thứ hai:\n{weapon2.name} | Loại: {type(weapon2).__name__} | Sát thương: {weapon2.calculate_total_damage()}"
    )

    if weapon1 > weapon2:

        print(
            f"\nKết quả: {weapon1.name} mạnh hơn {weapon2.name}."
        )

    elif weapon2 > weapon1:

        print(
            f"\nKết quả: {weapon2.name} mạnh hơn {weapon1.name}."
        )

    else:

        print(
            "\nKết quả: Hai vũ khí có sức mạnh ngang nhau."
        )


def fuse_weapons():

    print(
        "\n--- DUNG HỢP VŨ KHÍ ---"
    )

    if len(inventory) < 2:

        print(
            "Cần ít nhất 2 vũ khí trong kho để dung hợp!"
        )

        return

    weapon1 = inventory[0]
    weapon2 = inventory[1]

    new_weapon = weapon1 + weapon2

    inventory.pop(0)
    inventory.pop(0)

    inventory.append(new_weapon)

    print(
        ">> Dung hợp vũ khí thành công!"
    )

    print(
        f"Vũ khí mới: {new_weapon.name}"
    )

    print("Loại: Weapon")

    print(
        f"Cấp cường hóa: {new_weapon.upgrade_level}"
    )

    print(
        f"Sát thương tổng: {new_weapon.calculate_total_damage()}"
    )


while True:

    print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")

    print("1. Xem kho vũ khí & Sát thương tổng")
    print("2. Rèn Vũ khí Vật lý")
    print("3. Rèn Kiếm Ma Thuật")
    print("4. Thẩm định vũ khí")
    print("5. Dung hợp vũ khí")
    print("6. Thoát game")
    
    choice = input("Chọn chức năng (1-6): ")

    match choice:

        case "1":
            show_inventory()

        case "2":
            forge_weapon()

        case "3":
            forge_magic_sword()

        case "4":
            compare_weapons()

        case "5":
            fuse_weapons()

        case "6":
            print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")