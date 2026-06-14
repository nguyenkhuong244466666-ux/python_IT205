import logging

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)


def display_matches(match_list):
    """Hiển thị danh sách trận đấu."""

    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10} {'Đội A':<15} {'Đội B':<15} {'Tỷ số':<10} {'Trạng thái'}")

    for match in match_list:
        try:
            print(
                f"{match['match_id']:<10} "
                f"{match['team_a']:<15} "
                f"{match['team_b']:<15} "
                f"{str(match['score_a']) + '-' + str(match['score_b']):<10} "
                f"{match['status']}"
            )
        except KeyError:
            print("Dữ liệu trận đấu bị thiếu.")

    logging.info("User viewed the match list.")


def add_match(match_list):
    """Thêm trận đấu mới."""

    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    for match in match_list:
        if match["match_id"].lower() == match_id.lower():
            print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
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
    logging.info(f"Match {match_id} added successfully")


def update_score(match_list):
    """Cập nhật tỷ số trận đấu."""

    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()

    for match in match_list:

        if match["match_id"].lower() == match_id.lower():

            print(
                f"Trận đấu: {match['team_a']} vs {match['team_b']} ({match['status']})"
            )

            while True:
                try:
                    score_a = int(input("Nhập điểm Đội A: "))

                    if score_a < 0:
                        print("Điểm số phải lớn hơn hoặc bằng 0.")
                        logging.error(f"Negative score input detected: {score_a}")
                        continue

                    break

                except ValueError as error:
                    print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
                    logging.error(f"Invalid score input. Error: {error}")

            while True:
                try:
                    score_b = int(input("Nhập điểm Đội B: "))

                    if score_b < 0:
                        print("Điểm số phải lớn hơn hoặc bằng 0.")
                        logging.error(f"Negative score input detected: {score_b}")
                        continue

                    break

                except ValueError as error:
                    print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
                    logging.error(f"Invalid score input. Error: {error}")

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

            print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
            logging.info(f"Match {match_id} score updated successfully")
            return

    print(f"Không tìm thấy trận đấu mang mã {match_id}.")
    logging.warning(f"User tried to update non-existing match {match_id}")


def determine_winner(match):
    """Trả về đội thắng."""

    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def generate_report(match_list):
    """Tạo báo cáo giải đấu."""

    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")

    completed_count = 0

    for match in match_list:

        if match["status"] == "Completed":

            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} "
                f"{match['score_a']}-{match['score_b']} "
                f"{match['team_b']} | "
                f"Kết quả: {winner}"
            )

            completed_count += 1

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"\nTổng số trận đã hoàn thành: {completed_count}")

    logging.info("User generated tournament report.")


def main():
    """Hàm chính."""

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

    while True:

        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ")

        match choice:

            case "1":
                display_matches(matches)

            case "2":
                add_match(matches)

            case "3":
                update_score(matches)

            case "4":
                generate_report(matches)

            case "5":
                logging.info("System closed.")
                print("Đã thoát chương trình.")
                break

            case _:
                print("Lựa chọn không hợp lệ!")
                logging.warning("Invalid menu choice selected")


main()