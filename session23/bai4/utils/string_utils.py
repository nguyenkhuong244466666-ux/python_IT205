def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")

    for student in records:
        name = " ".join(student["name"].split())
        student["name"] = name.title()

        print(
            f"{student['student_id']}: "
            f"{student['name']}"
        )

    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")