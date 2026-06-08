available_seats = 50
flight_revenue = 0.0

BASE_PRICE = 2000.0
MAX_SEATS = 50


def calculate_ticket_cost(quantity, ticket_class):
    """
    quantity (int): số lượng vé
    ticket_class (int): 1-Economy, 2-Business

    return (float): tổng tiền sau khi cộng phí dịch vụ
    """

    if ticket_class == 1:
        ticket_price = BASE_PRICE
        class_name = "Economy"
    else:
        ticket_price = BASE_PRICE * 1.5
        class_name = "Business"

    subtotal = quantity * ticket_price
    service_fee = subtotal * 0.05
    total_payment = subtotal + service_fee

    return total_payment, subtotal, service_fee, class_name


def book_tickets(quantity, total_payment):
    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return

    available_seats -= quantity
    flight_revenue += total_payment

    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")


def cancel_tickets(quantity):
    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_SEATS:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return

    refund_money = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_money

    return refund_money


def display_flight_status():
    """
    Hiển thị báo cáo tình trạng chuyến bay:
    - Sức chứa tối đa
    - Ghế đã đặt
    - Ghế trống
    - Tổng doanh thu
    """

    booked_seats = MAX_SEATS - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_SEATS}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")
    print("-----------------------------------")


while True:
    print("\n============= SKYBOOKING SYSTEM =============")
    print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
    print("1. Đặt vé máy bay")
    print("2. Hủy vé & Hoàn tiền")
    print("3. Xem tình trạng chuyến bay")
    print("4. Đóng hệ thống")
    print("=============================================")

    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            print("\n--- ĐẶT VÉ MÁY BAY ---")

            quantity = int(input("Nhập số lượng vé: "))

            if quantity <= 0:
                print("Số lượng vé không hợp lệ.")
                continue

            ticket_class = int(
                input("Chọn hạng vé (1: Economy, 2: Business): ")
            )

            if ticket_class not in [1, 2]:
                print("Hạng vé không hợp lệ.")
                continue

            total_payment, subtotal, service_fee, class_name = \
                calculate_ticket_cost(quantity, ticket_class)

            print("-> Xác nhận đặt chỗ:")
            print(f"Số lượng: {quantity} | Hạng: {class_name}")
            print(f"Tạm tính: ${subtotal}")
            print(f"Phí dịch vụ (5%): ${service_fee}")
            print(f"Tổng thanh toán: ${total_payment}")

            book_tickets(quantity, total_payment)

        case "2":
            print("\n--- HỦY VÉ & HOÀN TIỀN ---")

            quantity = int(input("Nhập số lượng vé muốn hủy: "))

            if quantity <= 0:
                print("Số lượng vé không hợp lệ.")
                continue

            refund_money = cancel_tickets(quantity)

            if refund_money is not None:
                print(
                    f"Hủy vé thành công. Hệ thống đã hoàn lại: "
                    f"${refund_money} (80% giá cơ bản)."
                )
                print(f"Ghế trống hiện tại: {available_seats}")

        case "3":
            display_flight_status()

        case "4":
            print("Đóng hệ thống thành công!")
            break

        case _:
            print("Lựa chọn không hợp lệ.")