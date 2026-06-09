def get_validate_input(prompt, input_type="str"):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Dữ liệu không được để trống!")
            continue

        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu phải lớn hơn 0!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                continue

        return user_input


def classify_status(empty_seats, total_seats):
    if empty_seats == 0:
        return "Hết vé"

    rate = empty_seats / total_seats

    if rate < 0.15:
        return "Hút khách"
    elif rate <= 0.8:
        return "Bình thường"
    else:
        return "Ế khách"


def update_trip_info(trip):
    sold_seats = trip["total_seats"] - trip["empty_seats"]

    trip["revenue"] = trip["ticket_price"] * sold_seats

    trip["status"] = classify_status(
        trip["empty_seats"],
        trip["total_seats"]
    )


def menu():
    print("\n" + "=" * 90)
    print("QUẢN LÝ CHUYẾN XE")
    print("1. Hiển thị danh sách chuyến xe")
    print("2. Thêm chuyến xe")
    print("3. Đặt vé")
    print("4. Xóa chuyến xe")
    print("5. Tìm kiếm chuyến xe")
    print("6. Thống kê trạng thái")
    print("7. Thoát")
    print("=" * 90)


def show_trips(trips):
    if not trips:
        print("Danh sách chuyến xe đang trống!")
        return

    print(
        f"{'MÃ':<10}"
        f"{'TUYẾN ĐƯỜNG':<30}"
        f"{'GIÁ VÉ':<15}"
        f"{'GHẾ TRỐNG':<12}"
        f"{'TỔNG GHẾ':<12}"
        f"{'DOANH THU':<15}"
        f"{'TRẠNG THÁI'}"
    )

    for trip in trips:
        print(
            f"{trip['id']:<10}"
            f"{trip['route']:<30}"
            f"{trip['ticket_price']:<15}"
            f"{trip['empty_seats']:<12}"
            f"{trip['total_seats']:<12}"
            f"{trip['revenue']:<15}"
            f"{trip['status']}"
        )


def add_trip(trips):
    while True:
        trip_id = get_validate_input("Nhập mã chuyến xe: ").upper()

        for trip in trips:
            if trip["id"] == trip_id:
                print("Mã chuyến xe đã tồn tại!")
                break
        else:
            break

    route = get_validate_input("Nhập tuyến đường: ")

    ticket_price = get_validate_input(
        "Nhập giá vé: ",
        "int"
    )

    total_seats = get_validate_input(
        "Nhập tổng số ghế: ",
        "int"
    )

    new_trip = {
        "id": trip_id,
        "route": route,
        "ticket_price": ticket_price,
        "empty_seats": total_seats,
        "total_seats": total_seats,
        "revenue": 0,
        "status": classify_status(total_seats, total_seats)
    }

    trips.append(new_trip)

    print("Thêm chuyến xe thành công!")


def book_ticket(trips):
    if not trips:
        print("Danh sách chuyến xe đang trống!")
        return

    trip_id = get_validate_input(
        "Nhập mã chuyến xe: "
    ).upper()

    for trip in trips:
        if trip["id"] == trip_id:

            quantity = get_validate_input(
                "Nhập số vé muốn đặt: ",
                "int"
            )

            if quantity > trip["empty_seats"]:
                print("Số vé vượt quá ghế trống!")
                return

            trip["empty_seats"] -= quantity

            update_trip_info(trip)

            print("Đặt vé thành công!")
            return

    print("Không tìm thấy chuyến xe!")


def delete_trip(trips):
    if not trips:
        print("Danh sách chuyến xe đang trống!")
        return

    trip_id = get_validate_input(
        "Nhập mã chuyến xe cần xóa: "
    ).upper()

    for index, trip in enumerate(trips):
        if trip["id"] == trip_id:

            confirm = input(
                "Bạn có chắc muốn xóa? (Y/N): "
            ).upper()

            if confirm == "Y":
                trips.pop(index)
                print("Xóa thành công!")
            else:
                print("Đã hủy thao tác!")

            return

    print("Không tìm thấy chuyến xe!")



def main():
    trips = []

    while True:
        menu()

        choice = input("Nhập lựa chọn: ")

        match choice:
            case "1":
                show_trips(trips)

            case "2":
                add_trip(trips)

            case "3":
                book_ticket(trips)

            case "4":
                delete_trip(trips)

            case "5":
                print()

            case "6":
                print()

            case "7":
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")
main()