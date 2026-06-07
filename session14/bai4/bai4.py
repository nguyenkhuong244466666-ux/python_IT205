student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (
        student["math"]
        + student["physics"]
        + student["chemistry"]
    ) / 3


def get_rank(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def find_student(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None


def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_rank(average)

        print(
            f"{index}. [{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------")


def update_student_score(records):
    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    student = find_student(records, student_id)

    if student is None:
        print(
            f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!"
        )
        return

    subject = input(
        "Chọn môn học (1-Toán, 2-Lý, 3-Hóa): "
    )

    while True:
        try:
            score = float(input("Nhập điểm mới: "))

            if 0 <= score <= 10:
                break

            print(
                "Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!"
            )

        except ValueError:
            print(
                "Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!"
            )

    match subject:
        case "1":
            student["math"] = score
            print(
                f">> Đã cập nhật điểm Toán của sinh viên "
                f"'{student['name']}' thành {score}."
            )

        case "2":
            student["physics"] = score
            print(
                f">> Đã cập nhật điểm Lý của sinh viên "
                f"'{student['name']}' thành {score}."
            )

        case "3":
            student["chemistry"] = score
            print(
                f">> Đã cập nhật điểm Hóa của sinh viên "
                f"'{student['name']}' thành {score}."
            )

        case _:
            print("Môn học không hợp lệ!")


def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    pass_count = 0
    fail_count = 0

    for student in records:
        average = calculate_average(student)

        if average >= 5:
            pass_count += 1
        else:
            fail_count += 1

    pass_percent = (pass_count / total) * 100
    fail_percent = (fail_count / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{pass_count} sinh viên "
        f"(Chiếm {pass_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{fail_count} sinh viên "
        f"(Chiếm {fail_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    highest_avg = calculate_average(top_student)

    for student in records:
        average = calculate_average(student)

        if average > highest_avg:
            highest_avg = average
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} "
        f"(Mã: {top_student['student_id']})"
    )
    print(f"Điểm Trung Bình: {highest_avg:.2f}")
    print(
        "Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!"
    )
    print("--------------------------")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")

    choice = input("Chọn chức năng (1-5): ")

    match choice:
        case "1":
            display_grades(student_records)

        case "2":
            update_student_score(student_records)

        case "3":
            generate_report(student_records)

        case "4":
            find_valedictorian(student_records)

        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")