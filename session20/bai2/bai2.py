# Dữ liệu API
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    """
    Tính điểm thưởng cuối mùa.

    Bonus = (matches * 10) + (mmr * 0.5)
    """
    return (matches * 10) + (mmr * 0.5)


def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:

        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]

            bonus = calculate_bonus(
                matches,
                int(mmr)
            )

            print(
                f"Tuyển thủ {name} nhận được {bonus} RP"
            )

        except IndexError:
            print(
                f"Tuyển thủ {record[0]}: "
                f"Lỗi - Hồ sơ bị thiếu thông tin!"
            )
            continue

        except ValueError:
            print(
                f"Tuyển thủ {record[0]}: "
                f"Lỗi - Dữ liệu MMR không hợp lệ!"
            )
            continue

    print("--- HOÀN TẤT ---")


process_bonus(player_records)