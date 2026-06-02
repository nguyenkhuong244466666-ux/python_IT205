order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng: ").strip()

    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for index, value in enumerate(order_list, start=1):
                    print(f"{index}. {value}")

        case "2":
            new_order_id = input("Nhập mã đơn hàng mới: ").strip().upper()

            if new_order_id == "":
                print("Mã đơn hàng không được để trống!")
            else:
                order_list.append(new_order_id)
                print("Thêm đơn hàng thành công.")

        case "3":
            delete_order_id = input("Nhập mã đơn hàng cần xóa: ").strip().upper()

            if delete_order_id in order_list:
                order_list.remove(delete_order_id)
                print("Xóa đơn hàng thành công.")
            else:
                print("Không tìm thấy mã đơn hàng cần xóa!")

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")