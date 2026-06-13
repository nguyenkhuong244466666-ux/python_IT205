matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


def find_match(match_list, match_id):
    for match in match_list:
        if match["match_id"] == match_id:
            return match
    return None


def determine_winner(match):
    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def display_matches(match_list):
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")

    for match in match_list:
        print(
            f"{match['match_id']} | "
            f"{match['team_a']} vs {match['team_b']} | "
            f"{match['score_a']}-{match['score_b']} | "
            f"{match['status']}"
        )


def add_match(match_list):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận: ").strip().upper()

    if match_id == "":
        print("Mã trận không được để trống.")
        return

    if find_match(match_list, match_id):
        print("Mã trận đã tồn tại.")
        return

    team_a = input("Nhập đội A: ").strip()
    team_b = input("Nhập đội B: ").strip()

    if team_a == "" or team_b == "":
        print("Tên đội không được để trống.")
        return

    match_list.append({
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    })

    print("Thêm trận đấu thành công!")


def input_score(team):
    while True:
        try:
            score = int(input(f"Nhập điểm {team}: "))

            if score < 0:
                print("Điểm phải >= 0")
                continue

            return score

        except ValueError:
            print("Điểm phải là số nguyên.")


def update_score(match_list):
    print("\n--- CẬP NHẬT TỶ SỐ ---")

    match_id = input("Nhập mã trận: ").strip().upper()

    match = find_match(match_list, match_id)

    if match is None:
        print("Không tìm thấy trận đấu.")
        return

    score_a = input_score("Đội A")
    score_b = input_score("Đội B")

    match["score_a"] = score_a
    match["score_b"] = score_b

    if score_a == 0 and score_b == 0:
        confirm = input(
            "Xác nhận hoàn thành? (y/n): "
        ).lower()

        if confirm == "y":
            match["status"] = "Completed"
        else:
            match["status"] = "Pending"
    else:
        match["status"] = "Completed"

    print("Cập nhật thành công!")


def generate_report(match_list):
    print("\n--- BÁO CÁO ---")

    count = 0

    for match in match_list:
        if match["status"] == "Completed":

            winner = determine_winner(match)

            print(
                f"{match['match_id']} | "
                f"Kết quả: {winner}"
            )

            count += 1

    print(f"Tổng số trận hoàn thành: {count}")


while True:
    print("\n===== MENU =====")
    print("1. Hiển thị")
    print("2. Thêm trận")
    print("3. Cập nhật tỷ số")
    print("4. Báo cáo")
    print("5. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        display_matches(matches)

    elif choice == "2":
        add_match(matches)

    elif choice == "3":
        update_score(matches)

    elif choice == "4":
        generate_report(matches)

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ.")