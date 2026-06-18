from abc import ABC, abstractmethod


class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ trong game.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Tính sát thương kỹ năng.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực tổng hợp.
        """
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        """
        Nạp chồng toán tử +
        """
        if isinstance(other, Champion):
            return (
                self.get_combat_power()
                + other.get_combat_power()
            )

        if isinstance(other, (int, float)):
            return other + self.get_combat_power()

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        """
        Nạp chồng toán tử >
        """
        return (
            self.get_combat_power()
            > other.get_combat_power()
        )


class Warrior(Champion):
    """
    Hệ Chiến Binh.
    """

    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        shield_bonus
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return (
            self.base_atk * 2
            + self.shield_bonus
        )


class Mage(Champion):
    """
    Hệ Pháp Sư.
    """

    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        ability_power
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return (
            self.base_atk
            * self.ability_power
        )


champion_pool = [
    Warrior(
        "WAR01",
        "Rikkei Knight",
        1200,
        300,
        150
    ),
    Warrior(
        "WAR02",
        "Steel Guardian",
        1500,
        250,
        200
    ),
    Mage(
        "MAG01",
        "Rikkei Wizard",
        800,
        500,
        2.0
    )
]


def find_champion(champion_id):
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion
    return None


def show_champions():
    print(
        "\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---"
    )

    print(
        f"{'Mã':<8}"
        f"{'Tên tướng':<20}"
        f"{'Hệ':<10}"
        f"{'HP':<8}"
        f"{'ATK':<8}"
        f"{'Chỉ số riêng':<20}"
        f"{'Chiến lực'}"
    )

    print("-" * 100)

    for champion in champion_pool:

        if isinstance(champion, Warrior):
            role = "Warrior"
            extra = (
                f"Armor: "
                f"{champion.shield_bonus}"
            )

        else:
            role = "Mage"
            extra = (
                f"Mana: "
                f"{champion.ability_power}"
            )

        print(
            f"{champion.champion_id:<8}"
            f"{champion.name:<20}"
            f"{role:<10}"
            f"{champion.base_hp:<8}"
            f"{champion.base_atk:<8}"
            f"{extra:<20}"
            f"{champion.get_combat_power():.0f}"
        )

    print("-" * 100)


def add_champion():

    print("\n1. Warrior")
    print("2. Mage")

    champion_type = input(
        "Chọn hệ tướng: "
    )

    champion_id = input(
        "Nhập mã tướng: "
    ).upper()

    if find_champion(champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input(
        "Nhập tên tướng: "
    )

    try:
        base_hp = int(
            input("Nhập HP: ")
        )

        base_atk = int(
            input("Nhập ATK: ")
        )

    except ValueError:
        print(
            "Dữ liệu HP hoặc ATK không hợp lệ!"
        )
        return

    if champion_type == "1":

        try:
            shield_bonus = int(
                input("Nhập Armor: ")
            )
        except ValueError:
            print(
                "Armor không hợp lệ!"
            )
            return

        champion = Warrior(
            champion_id,
            name,
            base_hp,
            base_atk,
            shield_bonus
        )

        champion_pool.append(champion)

        print(
            "\nThêm tướng Warrior thành công!"
        )

    elif champion_type == "2":

        try:
            ability_power = float(
                input(
                    "Nhập Ability Power: "
                )
            )
        except ValueError:
            print(
                "Ability Power không hợp lệ!"
            )
            return

        champion = Mage(
            champion_id,
            name,
            base_hp,
            base_atk,
            ability_power
        )

        champion_pool.append(champion)

        print(
            "\nThêm tướng Mage thành công!"
        )

    else:
        print("Lựa chọn không hợp lệ!")
        return

    print(
        f"Mã: {champion.champion_id}"
        f" | Tên: {champion.name}"
        f" | Chiến lực: "
        f"{champion.get_combat_power():.0f}"
    )


def compare_champions():

    print(
        "\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---"
    )

    id1 = input(
        "Nhập mã tướng thứ nhất: "
    ).upper()

    id2 = input(
        "Nhập mã tướng thứ hai: "
    ).upper()

    champion1 = find_champion(id1)
    champion2 = find_champion(id2)

    if champion1 is None:
        print(
            f"Mã tướng {id1} "
            f"không hợp lệ, bỏ qua!"
        )
        return

    if champion2 is None:
        print(
            f"Mã tướng {id2} "
            f"không hợp lệ, bỏ qua!"
        )
        return

    print("\nThông tin so sánh:")

    print(
        f"{champion1.champion_id}"
        f" - {champion1.name}"
        f" | Chiến lực: "
        f"{champion1.get_combat_power():.0f}"
    )

    print(
        f"{champion2.champion_id}"
        f" - {champion2.name}"
        f" | Chiến lực: "
        f"{champion2.get_combat_power():.0f}"
    )

    if champion1 > champion2:
        print(
            f"Kết quả: "
            f"{champion1.champion_id}"
            f" - {champion1.name}"
            f" mạnh hơn "
            f"{champion2.champion_id}"
            f" - {champion2.name}."
        )

    else:
        print(
            f"Kết quả: "
            f"{champion2.champion_id}"
            f" - {champion2.name}"
            f" mạnh hơn "
            f"{champion1.champion_id}"
            f" - {champion1.name}."
        )


def calculate_team_power():

    print(
        "\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---"
    )

    champion_ids = input(
        "Nhập danh sách mã tướng, "
        "cách nhau bằng dấu phẩy: "
    )

    champion_ids = [
        item.strip().upper()
        for item in champion_ids.split(",")
    ]

    selected_team = []

    for champion_id in champion_ids:

        champion = find_champion(
            champion_id
        )

        if champion is None:
            print(
                f"Mã tướng {champion_id} "
                f"không hợp lệ, bỏ qua!"
            )
            continue

        selected_team.append(champion)

    if not selected_team:
        return

    print("\nDanh sách đội hình:")

    for index, champion in enumerate(
        selected_team,
        start=1
    ):
        print(
            f"{index}. "
            f"{champion.champion_id}"
            f" - {champion.name}"
            f" | Chiến lực: "
            f"{champion.get_combat_power():.0f}"
        )

    total_power = sum(selected_team)

    print(
        f"\nTổng chiến lực đội hình: "
        f"{total_power:.0f}"
    )


while True:

    print(
        "\n===== RIKKEI RPG - AUTO BATTLER ====="
    )
    print(
        "1. Hiển thị bể tướng hiện có"
    )
    print(
        "2. Thêm quân cờ mới"
    )
    print(
        "3. So sánh 2 quân cờ"
    )
    print(
        "4. Tính tổng chiến lực đội hình"
    )
    print(
        "5. Thoát chương trình"
    )

    choice = input(
        "Chọn chức năng (1-5): "
    )

    match choice:

        case "1":
            show_champions()

        case "2":
            add_champion()

        case "3":
            compare_champions()

        case "4":
            calculate_team_power()

        case "5":
            print(
                "\nCảm ơn bạn đã sử dụng "
                "Rikkei RPG - Auto-Battler Manager!"
            )
            break

        case _:
            print(
                "Lựa chọn không hợp lệ!"
            )
