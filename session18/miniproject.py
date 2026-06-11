def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Dữ liệu không được để trống!")
            continue
        return value


def get_valid_price(prompt):
    while True:
        try:
            price = int(input(prompt))
            if price <= 0:
                print("Giá trị đơn hàng phải lớn hơn 0!")
                continue
            return price
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")


def show_orders(orders):
    if not orders:
        print("Hệ thống hiện chưa có đơn hàng nào!")
        return

    print("\nDANH SÁCH ĐƠN HÀNG ĐẠI LÝ")
    print("-" * 80)
    print(f"{'MÃ ĐƠN':<10} {'TÊN ĐẠI LÝ':<30} {'GIÁ TRỊ (VND)':>15} {'TRẠNG THÁI':>15}")
    print("-" * 80)

    for order in orders:
        print(
            f"{order['id']:<10} "
            f"{order['name']:<30} "
            f"{order['price']:>15,} "
            f"{order['status']:>15}"
        )


def add_order(orders):
    print("\nTẠO MỚI ĐƠN HÀNG")

    order_id = get_valid_string("Nhập mã đơn hàng: ").upper()

    for order in orders:
        if order["id"] == order_id:
            print("[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống! (ERR-01)")
            return

    agency_name = get_valid_string("Nhập tên đại lý: ")
    price = get_valid_price("Nhập giá trị đơn hàng (VND): ")

    new_order = {
        "id": order_id,
        "name": agency_name,
        "price": price,
        "status": "Unpaid"
    }

    orders.append(new_order)

    print(f"[Thành công]: Đơn hàng {order_id} đã được tạo thành công!")


def update_payment_status(orders):
    print("\nCẬP NHẬT TRẠNG THÁI THANH TOÁN")

    order_id = get_valid_string(
        "Nhập mã đơn hàng cần cập nhật: "
    ).upper()

    for order in orders:

        if order["id"] == order_id:

            if order["status"] == "Paid":
                print("[Lỗi]: Đơn hàng này đã được thanh toán trước đó! (ERR-04)")
                return

            print(
                f"Tìm thấy đơn hàng của: {order['name']} "
                f"(Giá trị: {order['price']:,})"
            )

            order["status"] = "Paid"

            print(
                f"[Thành công]: Đơn hàng {order_id} "
                f"đã được cập nhật trạng thái ĐÃ THANH TOÁN!"
            )
            return

    print(f"[Lỗi]: Không tìm thấy đơn hàng nào có mã [{order_id}]! (ERR-03)")


def calculate_revenue(orders):
    total_revenue = 0

    for order in orders:
        if order["status"] == "Paid":
            total_revenue += order["price"]

    discount_percent = 0

    if total_revenue >= 100_000_000:
        discount_percent = 5

    discount_money = total_revenue * discount_percent / 100

    return total_revenue, discount_percent, discount_money


def show_finance_report(orders):
    total_revenue, discount_percent, discount_money = calculate_revenue(orders)

    print("\nBÁO CÁO TÀI CHÍNH DOANH NGHIỆP")
    print(f"+ Tổng doanh thu thực tế (Đã thanh toán): {total_revenue:,} VND")
    print(f"+ Tỷ lệ chiết khấu áp dụng: {discount_percent}%")
    print(f"+ Số tiền chiết khấu đại lý nhận lại: {discount_money:,.0f} VND")


def menu():
    print("\n" + "=" * 50)
    print("QUẢN LÝ ĐƠN HÀNG - AGENT ORDER")
    print("1. Xem danh sách đơn hàng hiện có")
    print("2. Tạo mới đơn hàng đại lý")
    print("3. Cập nhật trạng thái thanh toán")
    print("4. Tính tổng doanh thu & Chiết khấu")
    print("5. Thoát chương trình")
    print("=" * 50)


def main():
    orders = [
        {
            "id": "HD01",
            "name": "Dai ly Hoang Long",
            "price": 45000000,
            "status": "Paid"
        },
        {
            "id": "HD02",
            "name": "Tap hoa Minh Thu",
            "price": 15000000,
            "status": "Unpaid"
        }
    ]

    while True:
        menu()

        try:
            choice = int(input("Mời chọn chức năng (1-5): "))

            match choice:

                case 1:
                    show_orders(orders)

                case 2:
                    add_order(orders)

                case 3:
                    update_payment_status(orders)

                case 4:
                    show_finance_report(orders)

                case 5:
                    print("Cảm ơn bạn đã sử dụng hệ thống!")
                    break

                case _:
                    print("Lựa chọn không hợp lệ!")

        except ValueError:
            print("Vui lòng nhập số từ 1 đến 5!")


main()