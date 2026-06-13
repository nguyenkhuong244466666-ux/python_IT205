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
    """
    Tìm trận đấu theo mã.
    Return:
        index nếu tìm thấy
        -1 nếu không tìm thấy
    """
    for index in range(len(match_list)):
        if match_list[index]["match_id"].upper() == match_id.upper():
            return index
    return -1


def display_matches(match_list):
    """
    Hiển thị danh sách trận đấu.
    """
    if len(match_list) == 0:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10}{'Đội A':<15}{'Đội B':<15}{'Tỷ số':<10}{'Trạng thái'}")
    print("-" * 65)

    for match in match_list:
        try:
            score = f"{match['score_a']}-{match['score_b']}"

            print(
                f"{match['match_id']:<10}"
                f"{match['team_a']:<15}"
                f"{match['team_b']:<15}"
                f"{score:<10}"
                f"{match['status']}"
            )

        except KeyError:
            print("Dữ liệu trận đấu bị thiếu!")


def add_match(match_list):
    """
    Thêm trận đấu mới.
    """
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip().upper()

    if match_id == "":
        print("Mã trận đấu không được để trống.")
        return

    if find_match(match_list, match_id) != -1:
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        return

    team_a = input("Nhập tên Đội A: ").strip()

    if team_a == "":
        print("Tên đội không được để trống.")
        return

    team_b = input("Nhập tên Đội B: ").strip()

    if team_b == "":
        print("Tên đội không được để trống.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }

    match_list.append(new_match)

    print(f"Thành công: Đã thêm trận đấu {match_id}.")


def input_score(team_name):
    """
    Nhập điểm hợp lệ.
    """
    while True:
        try:
            score = int(input(f"Nhập điểm {team_name}: "))

            if score < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                continue

            return score

        except ValueError:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")


def update_score(match_list):
    """
    Cập nhật tỷ số trận đấu.
    """
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip().upper()

    index = find_match(match_list, match_id)

    if index == -1:
        print(f"Không tìm thấy trận đấu mang mã {match_id}.")
        return

    match = match_list[index]

    print(
        f"\nTrận đấu: {match['team_a']} vs "
        f"{match['team_b']} ({match['status']})"
    )

    score_a = input_score("Đội A")
    score_b = input_score("Đội B")

    status = "Pending"

    if score_a == 0 and score_b == 0:
        confirm = input(
            "Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): "
        ).lower()

        if confirm == "y":
            status = "Completed"

    else:
        status = "Completed"

    match["score_a"] = score_a
    match["score_b"] = score_b
    match["status"] = status

    print(f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}.")


def determine_winner(match):
    """
    Xác định đội chiến thắng.
    """

    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def generate_report(match_list):
    """
    Báo cáo thống kê.
    """
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")

    completed_count = 0

    for match in match_list:

        if match["status"] == "Completed":

            completed_count += 1

            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} "
                f"{match['score_a']}-{match['score_b']} "
                f"{match['team_b']} | "
                f"Kết quả: {winner}"
            )

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"\nTổng số trận đã hoàn thành: {completed_count}")


def run_tests():
    """
    Test determine_winner()
    """
    print("\n===== UNIT TEST =====")

    test_1 = {
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 0,
        "status": "Completed"
    }

    print(
        "Test 1:",
        "PASS" if determine_winner(test_1) == "T1" else "FAIL"
    )

    test_2 = {
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 1,
        "score_b": 1,
        "status": "Completed"
    }

    print(
        "Test 2:",
        "PASS" if determine_winner(test_2) == "Draw" else "FAIL"
    )

    test_3 = {
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }

    print(
        "Test 3:",
        "PASS" if determine_winner(test_3) == "Not Started" else "FAIL"
    )

    print("===== KẾT THÚC TEST =====\n")


def main():
    """
    Hàm điều phối chương trình.
    """

    while True:

        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")

        try:
            choice = int(input("Chọn chức năng (1-5): "))

            match choice:

                case 1:
                    display_matches(matches)

                case 2:
                    add_match(matches)

                case 3:
                    update_score(matches)

                case 4:
                    generate_report(matches)

                case 5:
                    print("Cảm ơn bạn đã sử dụng hệ thống!")
                    break

                case _:
                    print("Lựa chọn không hợp lệ!")

        except ValueError:
            print("Vui lòng nhập số từ 1 đến 5!")


run_tests()
main()