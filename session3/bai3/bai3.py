print("===== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ =====")

for employee_number in range(1, 4):

    print("\n===== NHÂN VIÊN", employee_number, "=====")

    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập họ và tên nhân viên: ")
    department = input("Nhập phòng ban công tác: ")

    if employee_id.strip() == "" or employee_name.strip() == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ!")
        print("Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue

    print("\n===== HỒ SƠ NHÂN SỰ ĐIỆN TỬ =====")
    print("Mã nhân viên:", employee_id)
    print("Họ và tên:", employee_name)
    print("Phòng ban:", department)

print("\nĐã hoàn tất khởi tạo hồ sơ cho 3 nhân viên!")