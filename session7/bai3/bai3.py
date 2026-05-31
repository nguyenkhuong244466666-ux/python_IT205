raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":

        print("\nDỮ LIỆU GỐC:")
        print(raw_data)

    elif choice == "2":

        print("\n===== BÁO CÁO NHÂN SỰ =====")
        print(f"{'ID':<12}{'HỌ TÊN':<25}{'SỐ ĐIỆN THOẠI':<20}{'PHÒNG BAN':<10}")

        employees = raw_data.split("|")

        for employee in employees:

            parts = employee.split(";")

            employee_id = parts[0].strip().upper()
            employee_name = parts[1].strip().title()
            phone = parts[2].strip().replace("-", "")
            department = parts[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[6:]
            else:
                phone = "Invalid Format"

            print(
                f"{employee_id:<12}"
                f"{employee_name:<25}"
                f"{phone:<20}"
                f"{department:<10}"
            )

    elif choice == "3":

        search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()

        found = False

        employees = raw_data.split("|")

        for employee in employees:

            parts = employee.split(";")

            employee_id = parts[0].strip().upper()
            employee_name = parts[1].strip().title()
            phone = parts[2].strip().replace("-", "")
            department = parts[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[6:]
            else:
                phone = "Invalid Format"

            if employee_id == search_id:

                print("\nTHÔNG TIN NHÂN VIÊN")
                print("ID:", employee_id)
                print("Họ tên:", employee_name)
                print("Số điện thoại:", phone)
                print("Phòng ban:", department)

                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == "4":

        print("Thoát chương trình")
        break

    else:

        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")