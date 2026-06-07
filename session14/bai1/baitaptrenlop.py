def menu():
    print("===== MENU =====")
    print("1. Nhập danh sách sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Tìm kiếm sinh viên theo tên")
    print("4. Thoát chương trình")


def input_std(students):
    num_std = int(input("Nhập số lượng sinh viên: "))
    for i in range(num_std):
        print(f"\nNhập sinh viên thứ {i + 1}")
        id_std = input("Nhập ID sinh viên: ")
        name_std = input("Nhập tên sinh viên: ")
        new_std = {
            "id": id_std,
            "name": name_std
        }
        students.append(new_std)
    print("Thêm sinh viên thành công!")


def show_std(students):
    if len(students) == 0:
        print("Danh sách sinh viên trống!")
        return
    print("DANH SÁCH SINH VIÊN")
    for index, value in enumerate(students, start=1):
        print(
            f"Sinh viên thứ {index}: "
            f"ID: {value.get('id')} - "
            f"Tên: {value.get('name')}"
        )


def search_std(students):
    if len(students) == 0:
        print("Danh sách sinh viên trống!")
        return
    keyword = input("Nhập tên cần tìm: ").lower()
    found = False
    print("KẾT QUẢ TÌM KIẾM")
    for index, value in enumerate(students, start=1):
        if keyword in value.get("name").lower():
            print(
                f"Sinh viên thứ {index}: "
                f"ID: {value.get('id')} - "
                f"Tên: {value.get('name')}"
            )
            found = True

    if not found:
        print("Không tìm thấy sinh viên!")


def main():
    students = []
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                input_std(students)
            case "2":
                show_std(students)
            case "3":
                search_std(students)
            case "4":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main() 