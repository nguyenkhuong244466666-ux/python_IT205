print("===== HỆ THỐNG CHUẨN HÓA MÃ ĐĂNG KÝ KHÓA HỌC =====")

registration_count = int(input("Nhập số lượng phiếu đăng ký: "))

if registration_count <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")

else:

    for registration in range(1, registration_count + 1):

        print(f"\nPhiếu đăng ký {registration}")

        registration_data = input(
            "Nhập thông tin (Họ tên | Khóa học | Mã học viên | Email): "
        )

        parts = registration_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirmation_code = (
            student_code + "_" + course_name.upper().replace(" ", "-")
        )

        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)