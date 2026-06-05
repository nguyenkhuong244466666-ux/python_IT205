staff = []
id = 0

while True:
    print("     QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("1. Thêm nhân viên mới: ")
    print("2. Danh sách nhân viên: ")
    print("3. Xóa nhân viên: ")
    print("4. Thoát")
    choice = input("==> nhập lựa chọn của bạn: ")

    match choice:
        case "1":
            while True:
                staff_name = input("Nhập tên nhân viên: ")
                if len(staff_name) == 0:
                    print("Tên không được để trống!!")
                else:
                    break

            while True:
                salary = input("Nhập lương nhân viên: ")
                if salary.isdigit():
                    salary = int(salary)
                else:
                    print("Lương phải là số và lớn hơn 0")
                    continue

                if salary > 0:
                    break

            id += 1

            staff.append({
                "id": id,
                "name": staff_name,
                "salary": salary
            })

        case "2":
            print("      DANH SÁCH NHÂN VIÊN")
            for value in staff:
                print(f"{value['id']} - {value['name']} - {value['salary']}")

        case "3":
            del_id = input("Nhập id cần xóa: ")
            if del_id.isdigit():
                del_id = int(del_id)
            else:
                print("id phải là số và lớn hơn 0")
                continue
            

        case "4":
            print("Đã thoát chương trình")
            break

        case _:
            print("Lựa chọn của bạn không hợp lệ!!")